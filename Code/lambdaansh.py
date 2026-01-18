import json
import boto3

def lambda_handler(event,context):
    
    # Let's move the file from s3 bucket to another folder in the same bucket
    s3_client = boto3.client('s3') # No need to sepcify the key and secret as we'll run this inside the AWS & it will use the role assigned to the lambda function
    bucket_name = 'anshbucket2026'

    source_key = 'trigger/data_1.csv'  # Hardcoded file name
    destination_key = 'destination/data_1.csv'  # Hardcoded destination

    copy_source = {'Bucket': bucket_name, 'Key': source_key}

    # Copy the file to the new location
    s3_client.copy(copy_source, bucket_name, destination_key)

    # Delete the original file
    s3_client.delete_object(Bucket=bucket_name, Key=source_key)

    return {
        'statusCode': 200,
        'body': json.dumps('File moved successfully!')
    }

