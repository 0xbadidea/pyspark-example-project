from pyspark.sql.functions import col, explode
from pyspark.sql.types import StructType, StructField, LongType, StringType, ArrayType
from dependencies.spark import start_spark


def flatten_nested_types(df):
    stack = [((), df)]
    columns = []
    arrays = []
    flatten_again = False

    while len(stack) > 0:
        parent, df_popped = stack.pop()
        for column_name, column_type in df_popped.dtypes:
            if column_type[:6] == "struct":
                projected_df = df_popped.select(column_name + ".*")
                stack.append((parent + (column_name,), projected_df))
            else:
                if column_type[:5] == "array":
                    arrays.append("_".join(parent + (column_name,)))
                columns.append(
                    col(".".join(parent + (column_name,))).alias(
                        "_".join(parent + (column_name,))
                        .replace("__VALUE", "_Value")
                        .replace("__", "_Attr_")
                    )
                )

    df_result = df.select(columns)

    # At this point of time, all the struct columns have been flattened. Explode
    # the array columns, one at a time.
    for array_column in arrays:
        df_result = df_result.withColumn(array_column, explode(array_column))
        if df_result.schema[array_column].dataType.simpleString()[:6] == "struct":
            flatten_again = True

    return df_result, flatten_again


def flatten_dataframe(df, output_table_name=None, epoch_id=None):
    flatten_again = True

    # Keep flattening the dataframe until a struct column remains.
    # This would only every happen if we have Array of Struct type data.
    # Arrays are exploded after all the flattening is done for the struct types,
    # therefore this would result in columns with struct types, which were not
    # flattened earlier.
    while flatten_again:
        df_result, flatten_again = flatten_nested_types(df)
        if flatten_again:
            df = df_result

    if output_table_name:
        df_result.write.format("delta").mode("append").saveAsTable(output_table_name)
    else:
        return df_result


my_schema = StructType(
    [
        StructField("id", LongType()),
        StructField("currency", StringType()),
        StructField("notes", ArrayType(LongType())),
        StructField(
            "country",
            StructType(
                [
                    StructField("name", StringType()),
                    StructField("capital", StringType()),
                    StructField(
                        "address",
                        StructType(
                            [
                                StructField("street", StringType()),
                                StructField("pin", LongType()),
                                StructField(
                                    "nested_array", ArrayType(LongType(), True)
                                ),
                            ]
                        ),
                    ),
                ]
            ),
        ),
    ]
)

spark, *_ = start_spark()

data = [
    (
        1,
        "euro",
        [10, 20, 50],
        {
            "name": "Italy",
            "capital": "Rome",
            "address": {"street": "e.u.road", "pin": 100000, "nested_array": [1, 2, 3]},
        },
    ),
    (
        2,
        "franc",
        [100, 500],
        {
            "name": "France",
            "capital": "Paris",
            "address": {
                "street": "macron road",
                "pin": 200000,
                "nested_array": [4, 5, 6],
            },
        },
    ),
    (
        3,
        "yen",
        [50, 25],
        {
            "name": "Japan",
            "capital": "Tokyo",
            "address": {"street": "hyunxian", "pin": 300000, "nested_array": [7, 8, 9]},
        },
    ),
]
df = spark.createDataFrame(data, schema=my_schema)
df_flattened = flatten_dataframe(df)
