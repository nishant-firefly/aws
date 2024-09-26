
#This Lambda function is triggered by API Gateway and processes HTTP requests.

import json
def lambda_handler(event, context):
    # Extract the HTTP method and body from API Gateway event
    method = event['httpMethod']
    body = json.loads(event.get('body', {}))

    # Respond based on the HTTP method
    if method == 'GET':
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'GET request received'})
        }
    elif method == 'POST':
        return {
            'statusCode': 200,
            'body': json.dumps({'message': 'POST request received', 'data': body})
        }
    else:
        return {
            'statusCode': 400,
            'body': json.dumps({'error': 'Unsupported method'})
        }
