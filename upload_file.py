import boto3

def upload_to_s3(file_name, bucket_name, object_name=None):
    s3 = boto3.client('s3')

    if object_name is None:
        object_name = file_name

    try:
        s3.upload_file(file_name, bucket_name, object_name)
        print("Upload successful!")
    except Exception as e:
        print("Error:", e)

# Change bucket name before running
upload_to_s3("test.txt", "your-bucket-name")
