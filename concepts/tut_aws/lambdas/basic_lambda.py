import json

def lambda_handler(event, context):
    # Print event details for logging
    print("Event:", json.dumps(event))

    # Return a simple message
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
