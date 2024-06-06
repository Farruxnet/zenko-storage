import boto3

endpoint_url = 'http://storage.201.uz'

access_key = 'accessKey'
secret_key = 'verySecretKey'
bucket_name = 'your-bucket-name'

s3 = boto3.client('s3', endpoint_url=endpoint_url, aws_access_key_id=access_key, aws_secret_access_key=secret_key)