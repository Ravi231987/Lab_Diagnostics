import psycopg2
import boto3

# Redshift connection details
REDSHIFT_HOST = "XXX.redshift.amazonaws.com"
REDSHIFT_PORT = 5439
REDSHIFT_USER = "user"
REDSHIFT_PASSWORD = "password"
REDSHIFT_DB = "db-name"
REDSHIFT_TABLE = "table"

# Set up the S3 client to retrieve the transformed data
s3_client = boto3.client('s3')
bucket_name = "bucket-name"
file_name = "transformed_data.json"

def lambda_handler(event, context):
    # Get the S3 object containing the transformed data
    s3_client.download_file(bucket_name, file_name, '/tmp/transformed_data.json')

    # Connect to Redshift
    conn = psycopg2.connect(
        dbname=REDSHIFT_DB,
        user=REDSHIFT_USER,
        password=REDSHIFT_PASSWORD,
        host=REDSHIFT_HOST,
        port=REDSHIFT_PORT
    )
    
    cursor = conn.cursor()
    
    # Define the SQL COPY command to load data into Redshift
    copy_sql = f"""
    COPY {REDSHIFT_TABLE}
    FROM 's3://{bucket_name}/{file_name}'
    IAM_ROLE 'arn:aws:iam::your-account-id:role/your-redshift-role'
    JSON 'auto';
    """
    
    # Execute the COPY command
    cursor.execute(copy_sql)
    
    # Commit and close the connection
    conn.commit()
    cursor.close()
    conn.close()

    return {
        'statusCode': 200,
        'body': 'Data loaded into Redshift successfully'
    }