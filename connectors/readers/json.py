# https://stackoverflow.com/questions/69405073/how-to-encrypt-a-json-field-and-then-read-that-field-back-into-the-json

""" Read a JSON file."""

from pyspark.sql.types import StructType, StructField, StringType
from pyspark.sql.functions import expr, col, from_json, lit


class JsonReader:  # pylint: disable=too-few-public-methods

    """Provides the read_json method to read a JSON file."""

    def __init__(  # pylint: disable=too-many-instance-attributes
        self,
        spark,
        path,
        *,
        schema=None,
        pii_columns=None,
        decryption_key=None,
        options=None,
    ):
        self.spark = spark
        self.path = path
        self.schema = schema
        self.pii_columns = pii_columns
        self.decryption_key = decryption_key
        self.options = options
        if self.options is None:
            self.options = {}
        self.cache = "_cache"

    def read_json(self, decrypt=False):
        """Read a JSON File from the path specified.
        Supported optional parameters can be found from the Spark documentation:
          [1]: https://jsonlines.org/
          [2]: https://spark.apache.org/docs/3.5.0/sql-data-sources-json.html
          [3]: https://spark.apache.org/docs/latest/sql-data-sources-generic-options.html
          [4]: https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrameReader.csv.html

        The same method can be used to read a json where some of the columns have
        been previous encypted using the AES-GCM algorithm. In this case, the
        decrypt parameter must be set to True to return the decrypted values.

        :param decrypt: Boolean value indicating whether the encrypted columns
        should be decrypted.
        :type decrypt: bool
        :return: A tuple of two DataFrames, the first one containing the valid
        records and the second one containing the invalid records.
        :rtype: (DataFrame, DataFrame)
        :raises: ValueError if decrypt is set to True and either the decryption
        key or the pii_columns are not provided.
        """  # pylint: disable=line-too-long

        if decrypt:
            if any(
                var is None or var == "None"
                for var in [self.pii_columns, self.decryption_key]
            ):
                raise ValueError("'pii_columns' and 'decryption_key' cannot be None.")

        # If schema is provided, parse the data according to the schema provided,
        # otherwise, infer the schema.
        if self.schema:
            # Get the name of the column containing the corrupt record.
            corrupt_record, column_present = self.__get_corrupt_record()

            # If the option 'columnNameOfCorruptRecord' is not set, set the same.
            if not column_present:
                self.options["columnNameOfCorruptRecord"] = corrupt_record

            # Inspect the schema to see if the 'corrupt_record' column identified
            # is present in the schema provided. If not, add it to the schema.
            schema = self.__create_corrupt_record_schema(corrupt_record)

            # If any of the columns have been encrypted previously and decryption
            # is requested, modify the schema to take into account the encrypted
            # columns.
            if decrypt:
                schema = self.__create_encrypted_schema(schema)
                df_json = self.__load_json(schema)
                df_json = self.__decrypt_encrypted_cols(df_json)
            else:
                # The data may contain encrypted columns, however decryption is not needed.
                # Return the encrypted values in the output dataframe.
                if self.pii_columns:
                    schema = self.__create_encrypted_schema(schema)
                df_json = self.__load_json(schema)

            df_valid = (
                df_json.where(col(corrupt_record).isNull())
                .drop(corrupt_record)
                .drop(self.cache)
            )

            # Construct a copy of the schema with all String columns.
            string_schema = self.__create_string_schema(schema)

            # pylint: disable=protected-access
            df_invalid = (
                df_json.where(col(corrupt_record).isNotNull())
                .select(
                    from_json(
                        corrupt_record,
                        self.spark.createDataFrame(
                            self.spark.sparkContext.emptyRDD(), string_schema
                        )
                        ._jdf.schema()
                        .toDDL(),
                        self.options,
                    ).alias(corrupt_record)
                )
                .select(f"{corrupt_record}.*")
                .drop(corrupt_record)
                .drop(self.cache)
            )

        else:
            # Read the csv file with the inferred schema and decrypt the columns if
            # required.
            self.options["inferSchema"] = True

            df_json = self.__load_json()
            if decrypt:
                df_json = self.__decrypt_encrypted_cols(df_json)

            df_valid = df_json.drop(self.cache)
            df_invalid = df_json.limit(0).drop(self.cache)

        return df_valid, df_invalid

    def __create_string_schema(self, schema):
        string_schema = StructType()
        for column in schema.fieldNames():
            string_schema = string_schema.add(StructField(column, StringType(), True))

        return string_schema

    def __get_corrupt_record(self):
        """Get the name of the corrupt record column. If not available,
        set the column to '_corrupt_record' and set an indicator for the same."""

        column_present = True
        if self.options and self.options.get("columnNameOfCorruptRecord"):
            corrupt_record = self.options.get("columnNameOfCorruptRecord")
        else:
            corrupt_record = "_corrupt_record"
            column_present = False

        return corrupt_record, column_present

    def __load_json(self, schema=None):
        """Read the json file with the updated options and schema as applicable."""
        if schema:
            df_json = (
                self.spark.read.format("json")
                .options(**self.options)
                .schema(schema)
                .load(self.path)
                .withColumn("source_file_name", col("_metadata.file_name"))
                .dropna("all")
                .withColumn(self.cache, lit(True))
                # .persist(StorageLevel.MEMORY_AND_DISK)
            )
        else:
            df_json = (
                self.spark.read.format("json")
                .options(**self.options)
                .load(self.path)
                .withColumn("source_file_name", col("_metadata.file_name"))
                .dropna("all")
                .withColumn(self.cache, lit(True))
                # .persist(StorageLevel.MEMORY_AND_DISK)
            )

        df_json.count()  # Force the cache.

        return df_json

    def __create_corrupt_record_schema(self, corrupt_record):
        """Update the schema with the corrupt record column."""

        schema = self.schema

        if corrupt_record not in self.schema.fieldNames():
            if isinstance(self.schema, StructType):
                schema = self.schema.add("_corrupt_record", StringType())
            elif "_corrupt_record" not in self.schema:
                schema += ",_corrupt_record string"

        return schema

    def __create_encrypted_schema(self, schema):
        """Create a schema with the data types for encrypted columns,
        converted into a StringType()"""

        encrypted_schema = StructType()
        for column in schema.fieldNames():
            if column in self.pii_columns:
                encrypted_schema.add(column, StringType())
            else:
                encrypted_schema.add(column, self.schema[column].dataType)

        return encrypted_schema

    def __decrypt_encrypted_cols(self, df_encrypted):
        """Read a csv file with PII columns, previously encrypted using the
        AES-GCM algorithm. The algorithm depends on the length of the key:
             16: AES-128
             24: AES-192
             32: AES-256
        Ref: [1]: https://learn.microsoft.com/en-gb/azure/databricks/sql/language-manual/functions/aes_decrypt
        """  # pylint: disable=line-too-long

        df_decrypted = df_encrypted

        for column in self.pii_columns:
            df_decrypted = df_decrypted.withColumn(
                column,
                expr(f"aes_decrypt(unbase64({column}), {self.decryption_key}, 'GCM')"),
            )

        return df_decrypted
