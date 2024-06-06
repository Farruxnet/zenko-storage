from config import s3

response = s3.list_buckets()

bucket_names = [bucket['Name'] for bucket in response['Buckets']]

print("Bucket List:")
for bucket_name in bucket_names:
    print(bucket_name)