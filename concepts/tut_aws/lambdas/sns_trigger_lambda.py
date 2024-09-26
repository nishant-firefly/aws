# This example shows how Lambda can be triggered when an SNS topic receives a new message.
# Step 1: Create an SNS Topic
# Create an SNS topic via the AWS CLI or console:
# $ aws sns create-topic --name MyTopic

import json

def lambda_handler(event, context):
    # Loop through SNS records
    for record in event['Records']:
        sns_message = record['Sns']['Message']
        print(f"Received SNS message: {sns_message}")

        # Process the SNS message
        try:
            data = json.loads(sns_message)
            print(f"Processed message: {data}")
        except Exception as e:
            print(f"Error processing SNS message: {e}")

    return {
        'statusCode': 200,
        'body': json.dumps('SNS messages processed successfully')
    }


# publish messages to the SNS topic using the AWS CLI:
# aws sns publish --topic-arn arn:aws:sns:us-east-1:123456789012:MyTopic --message '{"key": "value"}'
