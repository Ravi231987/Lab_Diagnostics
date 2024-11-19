import psycopg2
import boto3
from botocore.exceptions import ClientError
import json

def get_secret(secret_name, region_name="us-east-1"):
    # Create a Secrets Manager client
    client = boto3.client("secretsmanager", region_name=region_name)

    try:
        # Retrieve the secret value from Secrets Manager
        response = client.get_secret_value(SecretId=secret_name)
        
        # Secrets Manager decrypts the secret value automatically
        # If the secret is in the "SecretString" field, it's a plaintext string
        if "SecretString" in response:
            secret = response["SecretString"]
            # The secret is a JSON string, so we parse it
            secret_dict = json.loads(secret)
            return secret_dict  # Return the secret as a dictionary

    except ClientError as e:
        # Handle errors (e.g., if the secret is not found)
        print(f"Error retrieving secret: {e}")
        return None

# Example usage:
secret_name = "my-secret"  # Replace with your secret's name
secret = get_secret(secret_name)

# Redshift connection details
REDSHIFT_HOST = secret_name['host']
REDSHIFT_PORT = 5439
REDSHIFT_USER = secret_name['user']
REDSHIFT_PASSWORD = secret_name['pwd']
REDSHIFT_DB = secret_name['db-name']
REDSHIFT_TABLE = secret_name['table']

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