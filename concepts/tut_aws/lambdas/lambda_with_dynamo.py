import json
import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('MyDynamoDBTable')

def lambda_handler(event, context):
    # Write data to DynamoDB
    table.put_item(
        Item={
            'ID': '12345',
            'Name': 'John Doe',
            'Age': 30
        }
    )
    
    # Read data from DynamoDB
    response = table.query(
        KeyConditionExpression=Key('ID').eq('12345')
    )
    items = response['Items']

    return {
        'statusCode': 200,
        'body': json.dumps(items)
    }
