import os
import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.types import \
    StructType, StructField, \
    TimestampType, StringType, IntegerType, IntegerType

table_schema = StructType(
    [
        StructField("timestamp", TimestampType(), False),
        StructField("map_name", StringType(), False),
        StructField("attacker_name", StringType(), False),
        StructField("attacker_x", IntegerType(), False),
        StructField("attacker_y", IntegerType(), False),
        StructField("victim_x", IntegerType(), False),
        StructField("victim_y", IntegerType(), False),
        StructField("game_stage", IntegerType(), False),
        StructField("weapon_name", StringType(), False),
        StructField("zone_x", IntegerType(), False),
        StructField("zone_y", IntegerType(), False),
        StructField("zone_radius", IntegerType(), False),
        StructField("scope", StringType(), True),
        StructField("muzzle", StringType(), True)
    ]
)

session = SparkSession.builder \
    .master("spark://master:7077") \
    .appName("Weapon Ranking") \
    .getOrCreate()

print("Connected")

df = session.read.csv("hdfs://master:9000/data/Baltic_Main_data.txt", header=True, schema=table_schema, nullValue="None")

# drop non-existing scope and muzzles
df = df.filter(df.scope.isNotNull() & df.muzzle.isNotNull())

print(df.count())


session.stop()
