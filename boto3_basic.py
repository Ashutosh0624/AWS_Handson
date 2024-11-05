import boto3
from botocore.exceptions import ClientError
from param import Filename

s3  = boto3.resource('s3', region_name = 'ap-south-1')
bucket_name = 'november-bucket-sgrl-41124-1'

all_my_buckets = [bucket.name for bucket in s3.buckets.all()]

if bucket_name not in  all_my_buckets:
    print(f"{bucket_name} bucket does not exist")
    try:
        # Create a bucket with a specified location constraint
        s3.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={
                'LocationConstraint': 'ap-south-1'  # Specify the region here
            }
        )
        print(f"Bucket {bucket_name} created successfully.")
    except ClientError as e:
        print(f"Error creating bucket: {e}")

else:
    print(f"{bucket_name} bucket already exist")

# upload file
file_1 = 'file1.txt'
file_2 = 'file2.txt'
try:
    s3.Bucket(bucket_name).upload_file(Filename=file_1, Key=file_1)
    print(f"{file_1} has been successfully uploaded to the bucket")

    s3.Bucket(bucket_name).upload_file(Filename=file_2, Key=file_2)
    print(f"{file_1} has been successfully uploaded to the bucket")
except ClientError as e:
    print(f"error uploading the files: {e}")

# reading the file
obj = s3.Object(bucket_name, file_1)
body = obj.get()['Body'].read()
print(body)

obj2 = s3.Object(bucket_name, file_2)
body = obj2.get()['Body'].read()
print(body)

#update
s3.Object(bucket_name, file_1).put(Body = open(file_2, 'rb'))
obj = s3.Object(bucket_name, file_1)
body = obj.get()['Body'].read()
print(body)

# Delete operation
# first empty the bucket
s3.Object(bucket_name, file_1).delete()
s3.Object(bucket_name, file_2).delete()

# Delete the bucket
bucket = s3.Bucket(bucket_name)
bucket.delete()