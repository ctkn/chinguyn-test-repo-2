import sys
from pyspark.context import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql.dataframe import DataFrame
import pyspark.sql.functions as F

sc = SparkContext.getOrCreate()
spark = SparkSession.builder.getOrCreate()

# Script generated for node S3DataSource
S3DataSource_1787774784126 = spark.read.format("csv") \
    .option("inferschema", "true") \
    .option("multiLine", "true") \
    .option("header", "true") \
    .option("recursiveFileLookup", "true") \
    .option("sep", ",") \
    .load("s3://fdsa")
def split_string_list(slist):
    """
    Split a string with list of elements and return a list with those elements
    :param slist: string with tokens separated by commas
    :return: list of strings after the split, stripped of extra whitespace around it
    """
    return [x.strip() for x in slist.split(',')]
def is_blank_df(df):
    # Indicates if the DataFrame has no schema and no rows.
    return not df.schema.fieldNames() and not df.take(1)
def enrich_df(name, function):
    def transform_df(self, *args, **kwargs):
        if is_blank_df(self):
            return self  # No data to transform, return as is
        return function(self, *args, **kwargs)
    setattr(DataFrame, name, transform_df)
def uuid(self, colName="uuid"):
    return self.withColumn(colName, F.expr("uuid()"))
enrich_df('gs_uuid', uuid)
# Script generated for node UUIDTransformTransform
UUIDTransformTransform_1787774992720 = S3DataSource_1787774784126.gs_uuid("uuid")
