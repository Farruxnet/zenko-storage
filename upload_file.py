from config import s3, bucket_name

object_name = 'test.txt'
file_name = 'test.txt'

try:
    s3.upload_file(file_name, bucket_name, object_name)
    print(f"File '{file_name}' uploaded to bucket '{bucket_name}' as '{object_name}'.")
except Exception as e:
    print(f"Failed to upload file: {e}")