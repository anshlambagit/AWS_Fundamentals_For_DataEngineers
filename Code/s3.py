import boto3
from load_dotenv import load_dotenv
import os
load_dotenv()

s3_client = boto3.client('s3',
                         region_name='ca-central-1',
                         aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
                         aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY']
)

# List all S3 buckets
buckets = s3_client.list_buckets()
for bucket in buckets['Buckets']:
    print(f'Bucket Name: {bucket["Name"]}, Creation Date: {bucket["CreationDate"]}')

# Delete a specific S3 bucket
response = s3_client.delete_bucket(
    Bucket='your-bucket-name',
    ExpectedBucketOwner='123456789012'
)