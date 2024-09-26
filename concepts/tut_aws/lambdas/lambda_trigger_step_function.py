"""
{
  "StartAt": "HelloWorld",
  "States": {
    "HelloWorld": {
      "Type": "Pass",
      "Result": "Hello, World!",
      "End": true
    }
  }
}

"""
import json
import boto3

# Initialize the Step Functions client
stepfunctions = boto3.client('stepfunctions')

def lambda_handler(event, context):
    # Specify the ARN of the Step Function
    state_machine_arn = 'arn:aws:states:us-east-1:123456789012:stateMachine:MyStateMachine'

    # Define the input for the Step Function
    input_data = {
        "input_key": "input_value"
    }

    # Start the Step Function execution
    response = stepfunctions.start_execution(
        stateMachineArn=state_machine_arn,
        input=json.dumps(input_data)
    )

    # Log the response and execution ARN
    print(f"Step Function Execution ARN: {response['executionArn']}")

    return {
        'statusCode': 200,
        'body': json.dumps('Step Function invoked successfully')
    }
