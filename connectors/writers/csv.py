""" Write a CSV file."""

import shutil
import tempfile
import os

from pyspark.sql.functions import expr

class WriteCSV:  # pylint: disable=too-many-instance-attributes

    """Provides the write_csv method to write a CSV file."""

    def __init__(
        self,
        df_csv,
        file_path,
        file_name,
        *,
        pii_columns=None,
        encryption_key=None,
        mode="overwrite",
        delimiter=",",
        quote_char='"',
        escape_char="\\",
        **options,
    ):
        self.df_csv = df_csv
        self.file_path = file_path
        self.file_name = file_name
        self.pii_columns = pii_columns
        self.encryption_key = encryption_key
        self.mode = mode
        self.delimiter = delimiter
        self.quote_char = quote_char
        self.escape_char = escape_char
        self.options = options

    def write_csv(self):
        """Write a CSV File to the specified Azure ADLS location.
        Supported optional parameters can be found from the spark documentation:
        [1]: https://spark.apache.org/docs/3.5.0/sql-data-sources-csv.html
        [2]: https://spark.apache.org/docs/latest/sql-data-sources-generic-options.html
        [3]: https://spark.apache.org/docs/latest/api/python/reference/pyspark.sql/api/pyspark.sql.DataFrameWriter.csv.html
        """  # pylint: disable=line-too-long

        self.df_csv = self.df_csv.coalesce(1)
        df_writer = self.df_csv.write.format("csv").mode(self.mode)

        for key, value in self.options:
            df_reader = df_reader.option(key, value)

        with tempfile.TemporaryDirectory() as tmpdir:
            temp_filename = self.file_name + ".tmp"
            temp_filepath = tmpdir

            # Write the extract to a temporary CSV file.
            (
                df_writer.option("delimiter", self.delimiter)
                .option("quote", self.quote_char)
                .option("emptyValue", "")
                .option("escape", self.escape_char)
                .option("header", True)
                .option("ignoreLeadingWhiteSpace", False)
                .option("ignoreTrailingWhiteSpace", False)
                .save(os.path.join(temp_filepath, temp_filename))
            )

            # Extract the part file name.
            part_filename = [
                file.name
                for file in os.listdir(os.path.join(temp_filepath, temp_filename))
                if file.name.startswith("part-00000")
            ][0]

            # Move the part file to the desired location.
            shutil.move(
                "dbfs:" + os.path.join(temp_filepath, temp_filename, part_filename),
                os.path.join(self.file_path, "Rejected_" + self.file_name),
            )

            # Delete the temporary file path.
            shutil.rmtree("dbfs:" + os.path.join(temp_filepath, part_filename))

    def write_csv_with_pii(self):
        """Write a CSV file with PII columns, encrypted with a key.
        The algorithm depends on the length of the key:
            16: AES-128
            24: AES-192
            32: AES-256
        Ref: [1]: https://learn.microsoft.com/en-gb/azure/databricks/sql/language-manual/functions/aes_encrypt
        """  # pylint: disable=line-too-long

        # Encrypt the PII columns with the key provided, using AES-GCM algorithm.
        for column in self.pii_columns:
            self.df_csv = self.df_csv.withColumn(
                column,
                expr(f"aes_encrypt(base64({column}), {self.encryption_key}, 'GCM')"),
            )

        self.write_csv()
