# Lambda automatically logs events to CloudWatch. Here's how to log custom messages and metrics:

import json
import logging

# Setup logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    # Log the incoming event
    logger.info(f"Received event: {json.dumps(event)}")

    # Log a custom metric
    logger.info(f"Invoked Lambda function name: {context.function_name}")

    # Simulate processing and return a response
    return {
        'statusCode': 200,
        'body': json.dumps('Processed successfully!')
    }
