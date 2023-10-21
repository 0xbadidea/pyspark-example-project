""" Read a CSV file."""

import pyspark


class ReadCSV:

    """Provides the read_csv method to read a CSV file."""

    def __init__(
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

    def read_csv(self):
        """Read a CSV File from the path specified.
        Supported optional parameters can be found from the Spark documentation:
          [1]: https://spark.apache.org/docs/3.5.0/sql-data-sources-csv.html
          [2]: https://spark.apache.org/docs/latest/sql-data-sources-generic-options.html
          [3]: https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrameReader.csv.html
        """  # pylint: disable=line-too-long

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
                if isinstance(self.schema, pyspark.sql.types.StructType):
                    self.schema = self.schema.add(
                        "_corrupt_record", pyspark.sql.types.StringType()
                    )
                else:
                    if not "_corrupt_record" in self.schema:
                        self.schema += ",_corrupt_record string"

            df_reader = df_reader.schema(self.schema)
            df_csv = df_reader.load(self.path).persist(
                pyspark.StorageLevel.MEMORY_AND_DISK
            )
            df_valid = df_csv.where(df_csv["_corrupt_record"].isNull())
            df_invalid = df_csv.where(df_csv["_corrupt_record"].isNotNull())

        else:
            df_reader = df_reader.option("inferSchema", True)
            df_csv = df_reader.load(self.path)
            df_valid = df_csv
            df_invalid = df_csv.limit(0)

        return df_valid, df_invalid

    def read_csv_with_pii(self):
        """Read a csv file with PII columns, encrypted with a key. 
           The algorithm depends on the length of the key:
                16: AES-128
                24: AES-192
                32: AES-256
           Ref: [1]: https://learn.microsoft.com/en-gb/azure/databricks/sql/language-manual/functions/aes_decrypt
        """ # pylint: disable=line-too-long

        df_valid, df_invalid = self.read_csv()

        for column in self.pii_columns:
            df_valid = df_valid.withColumn(
                column,
                pyspark.sql.functions.expr(
                    f"aes_decrypt(unbase64({column}), {self.decryption_key}, 'GCM')"
                ),
            )

        for column in self.pii_columns:
            df_invalid = df_invalid.withColumn(
                column,
                pyspark.sql.functions.expr(
                    f"aes_decrypt(unbase64({column}), {self.decryption_key}, 'GCM')"
                ),
            )
        
        return df_valid, df_invalid
    