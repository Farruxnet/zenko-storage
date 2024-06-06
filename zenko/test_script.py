import boto3

# Specify your AWS Access Key ID and Secret Access Key here.
aws_access_key_id = 'accessKey'
aws_secret_access_key = 'verySecretKey'

# Initialize a session using Spaces
session = boto3.session.Session()

s3_client = session.client('s3',
                           region_name='us-east-1',
                           endpoint_url='http://localhost:9999',
                           aws_access_key_id=aws_access_key_id,
                           aws_secret_access_key=aws_secret_access_key)

# Create a new bucket
bucket_name = 'my-test-bucket'
s3_client.create_bucket(Bucket=bucket_name)

# Upload a file to the bucket
file_path = 'test_file_2.txt'
s3_client.upload_file(file_path, bucket_name, 'test_file_2.txt')

# List all files in the bucket
response = s3_client.list_objects_v2(Bucket=bucket_name)
for object in response['Contents']:
    print(object['Key'])

path = "violation/violation/macos.png"
Key = f"media/{path}"
fileobj = s3_client.get_object(Bucket=bucket_name, Key=Key)
filedata = fileobj['Body'].read()
print(filedata)
