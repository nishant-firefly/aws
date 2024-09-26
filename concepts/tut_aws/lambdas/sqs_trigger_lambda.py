# Create an SQS queue via the AWS console or CLI:

# $ aws sqs create-queue --queue-name MyQueue

# This Lambda function processes messages from an SQS queue.
import json

def lambda_handler(event, context):
    # Loop through the records in the SQS event
    for record in event['Records']:
        # Extract the body of the message
        message_body = record['body']
        print(f"Received message: {message_body}")

        # Process the message (example: print it)
        try:
            message = json.loads(message_body)
            print(f"Processing message: {message}")
        except Exception as e:
            print(f"Error processing message: {e}")

    return {
        'statusCode': 200,
        'body': json.dumps('Messages processed successfully')
    }

# Triggering Lambda with SQS:

# Configure the Lambda trigger to receive messages from the SQS queue using the AWS Console or CDK.