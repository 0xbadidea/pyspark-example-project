""" Read a CSV file."""

from pyspark.storagelevel import StorageLevel
from pyspark.sql.types import StructType, StringType
from pyspark.sql.functions import expr

#TODO: Rehaul the API design - https://benhoyt.com/writings/python-api-design/

class CSVReader:  # pylint: disable=too-few-public-methods

    """Provides the read_csv method to read a CSV file."""

    def __init__(  # pylint: disable=too-many-instance-attributes
        self,
        spark,
        path,
        /,
        schema=None,
        pii_columns=None,
        decryption_key=None,
        **options,
    ):
        self.spark = spark
        self.path = path
        self.schema = schema
        self.pii_columns = pii_columns
        self.decryption_key = decryption_key
        self.options = options

    def read_csv(self, decrypt=False):
        """Read a CSV File from the path specified.
        Supported optional parameters can be found from the Spark documentation:
          [1]: https://spark.apache.org/docs/3.5.0/sql-data-sources-csv.html
          [2]: https://spark.apache.org/docs/latest/sql-data-sources-generic-options.html
          [3]: https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrameReader.csv.html

        The same method can be used to read a csv where some of the columns have
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

        df_reader = self.spark.read.format("csv").option("mode", "PERMISSIVE")

        if self.options:
            if self.options.get("columnNameOfCorruptRecord") is None:
                df_reader = df_reader.option(
                    "columnNameOfCorruptRecord", "_corrupt_record"
                )
            else:
                corrupt_record = self.options.get("columnNameOfCorruptRecord")

            for key, value in self.options:
                df_reader = df_reader.option(key, value)
        else:
            df_reader = df_reader.option("columnNameOfCorruptRecord", "_corrupt_record")

        # If schema is provided, we parse the data and try to match it with the schema,
        # otherwise, we infer the schema and parse the data.
        if self.schema:
            if corrupt_record is None:
                if isinstance(self.schema, StructType):
                    self.schema = self.schema.add("_corrupt_record", StringType())
                else:
                    if "_corrupt_record" not in self.schema:
                        self.schema += ",_corrupt_record string"

            # If any of the columns have been encrypted previously and decryption
            # is requested, modify the schema to take into account the encrypted
            # columns.
            if decrypt:
                df_reader = df_reader.schema(self._create_encrypted_schema())
                df_csv = df_reader.load(self.path).persist(StorageLevel.MEMORY_AND_DISK)
                df_csv = self._decrypt_encrypted_cols(df_csv)
            else:
                # The data may contain encrypted columns, however decryption is not needed.
                # Return the encrypted values in the output dataframe.
                if self.pii_columns:
                    df_reader = df_reader.schema(self._create_encrypted_schema())
                else:
                    df_reader = df_reader.schema(self.schema)
                df_csv = df_reader.load(self.path).persist(StorageLevel.MEMORY_AND_DISK)

            df_valid = df_csv.where(df_csv["_corrupt_record"].isNull())
            df_invalid = df_csv.where(df_csv["_corrupt_record"].isNotNull())

        else:
            # Read the csv file with the inferred schema and decrypt the columns if
            # required.
            df_reader = df_reader.option("inferSchema", True)
            df_csv = df_reader.load(self.path)
            if decrypt:
                df_csv = self._decrypt_encrypted_cols(df_csv)

            df_valid = df_csv
            df_invalid = df_csv.limit(0)

        return df_valid, df_invalid

    def _create_encrypted_schema(self):
        """Create a schema with the data types for encrypted columns,
        converted into a StringType()"""

        encrypted_schema = StructType()
        for column in self.schema.fieldNames():
            if column in self.pii_columns:
                encrypted_schema.add(column, StringType())
            else:
                encrypted_schema.add(column, self.schema[column].dataType)

        return encrypted_schema

    def _decrypt_encrypted_cols(self, df_encrypted):
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
