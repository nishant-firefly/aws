"""
This example demonstrates handling errors in Lambda and how a DLQ (Dead Letter Queue) can be used to capture failed invocations.


"""
import json
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    try:
        # Simulate processing
        data = event['data']
        
        # Simulate an error
        if data == 'error':
            raise ValueError("Simulated error")

        logger.info("Processing successful")
        return {
            'statusCode': 200,
            'body': json.dumps('Success!')
        }

    except Exception as e:
        logger.error(f"Error occurred: {str(e)}")
        raise e  # Rethrow the error for DLQ to capture

"""
Configuring a Dead Letter Queue (DLQ):

In the AWS Lambda console, under the Asynchronous invocation settings, 
you can configure an SQS queue or an SNS topic as a DLQ to capture failed invocations.
"""