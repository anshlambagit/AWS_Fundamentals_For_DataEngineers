import boto3 

# Function to trigger the aws glue pipeline
def trigger_glue_pipeline(pipeline_name):
    glue_client = boto3.client('glue')
    
    try:
        response = glue_client.start_workflow_run(Name=pipeline_name)
        print(f"Glue pipeline '{pipeline_name}' triggered successfully. Run ID: {response['RunId']}")
    except Exception as e:
        print(f"Error triggering Glue pipeline: {e}")


import json
import boto3

def lambda_handler(event, context):
    
    glue_client = boto3.client('glue')

    glue_client.start_workflow_run(Name='demopipeline')

    return {
        'statusCode': 200,
        'body': json.dumps('Pipeline triggered')
    }
