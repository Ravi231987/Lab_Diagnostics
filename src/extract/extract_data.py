import json
import requests
import boto3
from datetime import datetime

# Set up S3 client
s3_client = boto3.client('s3')

# Define the S3 bucket where the raw data will be stored
bucket_name = "your-s3-bucket-name"

def lambda_handler(event, context):
    # Example API URL to fetch data (replace with your actual API endpoint)
    api_url = "https://api_url"
    
    # Make an API request
    response = requests.get(api_url)
    data = response.json()  # Assuming the API returns JSON
    
    # Generate a unique file name with a timestamp
    timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    file_name = f"raw_data_{timestamp}.json"
    
    # Save data to S3
    s3_client.put_object(
        Bucket=bucket_name,
        Key=file_name,
        Body=json.dumps(data)
    )
    
    return {
        'statusCode': 200,
        'body': json.dumps('Data extracted and stored successfully')
    }