from pyspark.sql.types import (
    StructType,
    StructField,
    StringType,
    IntegerType,
    DateType,
    BooleanType,
    DoubleType,
)

# TODO: Write Proper Unit Testing/ Integration Testing Code.
from dependencies.spark import start_spark
from connectors.readers.csv import CSVReader

# export PYTHONPATH="/workspaces/pyspark-example-project:$PYTHONPATH"

spark, *_ = start_spark()
schema = StructType(
    [
        StructField("spotify_id", StringType(), True),
        StructField("name", StringType(), True),
        StructField("artists", StringType(), True),
        StructField("daily_rank", IntegerType(), True),
        StructField("daily_movement", IntegerType(), True),
        StructField("weekly_movement", IntegerType(), True),
        StructField("country", StringType(), True),
        StructField("snapshot_date", DateType(), True),
        StructField("popularity", IntegerType(), True),
        StructField("is_explicit", BooleanType(), True),
        StructField("duration_ms", IntegerType(), True),
        StructField("album_name", StringType(), True),
        StructField("album_release_date", DateType(), True),
        StructField("danceability", DoubleType(), True),
        StructField("energy", DoubleType(), True),
        StructField("key", IntegerType(), True),
        StructField("loudness", DoubleType(), True),
        StructField("mode", IntegerType(), True),
        StructField("speechiness", DoubleType(), True),
        StructField("acousticness", DoubleType(), True),
        StructField("instrumentalness", DoubleType(), True),
        StructField("liveness", DoubleType(), True),
        StructField("valence", DoubleType(), True),
        StructField("tempo", DoubleType(), True),
        StructField("time_signature", IntegerType(), True),
        StructField("_corrupt_record", StringType(), True),
    ]
)

df_valid, df_invalid = CSVReader(
    spark,
    "tests/test_data/top_spotify_songs/universal_top_spotify_songs.csv",
    options={"header": True},
    schema=schema,
).read_csv()
print(df_valid.count())
print(df_invalid.count())

df_valid.show(10, truncate=False, vertical=True)
df_invalid.show(10, truncate=False, vertical=True)

print(df_valid.schema)
