from config import s3, bucket_name

response = s3.list_objects_v2(Bucket=bucket_name)

if 'Contents' in response:
    object_keys = [obj['Key'] for obj in response['Contents']]

    print("Files in Bucket:")
    for object_key in object_keys:
        print(object_key)
else:
    print("Bucket is empty")