import boto3

def download_from_s3(bucket_name, object_name, file_name=None):
    s3 = boto3.client('s3')

    if file_name is None:
        file_name = object_name

    try:
        s3.download_file(bucket_name, object_name, file_name)
        print("Download successful!")
    except Exception as e:
        print("Error:", e)

# Change bucket name before running
download_from_s3("your-bucket-name", "test.txt")
