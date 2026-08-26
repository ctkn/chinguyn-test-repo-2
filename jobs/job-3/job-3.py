import sys
from pyspark.context import SparkContext
from pyspark.sql import SparkSession

sc = SparkContext.getOrCreate()
spark = SparkSession.builder.getOrCreate()

# Script generated for node S3DataSource
S3DataSource_1781624523070 = spark.read.format("csv") \
    .option("inferschema", "true") \
    .option("multiLine", "true") \
    .option("header", "true") \
    .option("recursiveFileLookup", "true") \
    .option("sep", ",") \
    .load("s3://hdfbvjh")
