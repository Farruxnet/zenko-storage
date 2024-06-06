import boto3
from botocore.exceptions import ClientError

# Configuration
endpoint_url = 'http://storage.201.uz'  # Use 'http' if Nginx is listening on port 80
access_key = 'accessKey'
secret_key = 'verySecretKey'
bucket_name = 'your-bucket-name'

# Create S3 client
s3 = boto3.client('s3', endpoint_url=endpoint_url, aws_access_key_id=access_key, aws_secret_access_key=secret_key)

# Create bucket
try:
    s3.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
            'LocationConstraint': 'us-east-1'  # Optional: use appropriate region
        }
    )
    print(f"Bucket '{bucket_name}' created successfully.")
except ClientError as e:
    print(f"Error: {e}")