# This function is triggered when a file is uploaded to an S3 bucket. It logs the details of the uploaded object.

import json
import boto3

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    # Extract bucket and object key from the event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    # Log the details of the uploaded object
    print(f"File uploaded to S3 bucket: {bucket}, Object Key: {key}")

    # Optionally, perform operations like reading the file content
    response = s3_client.get_object(Bucket=bucket, Key=key)
    file_content = response['Body'].read().decode('utf-8')
    print(f"File Content: {file_content}")

    return {
        'statusCode': 200,
        'body': json.dumps('S3 file processed successfully!')
    }
