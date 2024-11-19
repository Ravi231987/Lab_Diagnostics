import boto3
import pandas as pd
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import json

# Initialize the Spark session (Glue provides this automatically in the environment)
spark = SparkSession.builder.appName("GlueETL").getOrCreate()

# Set up S3 client (optional, in case you want to interact directly with S3)
s3_client = boto3.client('s3')
bucket_name = "Bucket-name"

# Define paths for input and output data in S3
input_path = "s3://{}/raw_data/".format(bucket_name)
output_path = "s3://{}/transformed_data/".format(bucket_name)

def glue_job():
    # Read the raw data from S3 into a PySpark DataFrame
    # Glue automatically infers the schema of JSON files, so no need to define it explicitly
    raw_data_df = spark.read.json(input_path)
    
    # Perform transformations using PySpark DataFrame operations
    # Example: Drop rows with missing values in any column
    transformed_df = raw_data_df.dropna()

    # Example: Add a new column (e.g., 'processed_timestamp' with current timestamp)
    from pyspark.sql.functions import current_timestamp
    transformed_df = transformed_df.withColumn("processed_timestamp", current_timestamp())

    # Write the transformed DataFrame back to S3 (as JSON)
    transformed_df.write.json(output_path)

    # Optionally: You can also save it as other formats such as CSV, Parquet, or Avro
    # transformed_df.write.parquet("s3://your-s3-bucket-name/transformed_data_parquet/")

    return {
        'statusCode': 200,
        'body': 'Transformation and data writing to S3 completed successfully'
    }

# Run the glue job (in AWS Glue, this would run within the Glue job environment)
if __name__ == "__main__":
    glue_job()