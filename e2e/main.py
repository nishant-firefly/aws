import boto3
import os
from dotenv import load_dotenv
from step.examples_aws.hello_step_functions import hello_stepfunctions

dotenv_path = os.path.join(os.path.dirname(__file__), '..', 'up_system', '.env')
load_dotenv(dotenv_path)
print(dotenv_path, os.path.exists(dotenv_path))


hello_stepfunctions(boto3.client("stepfunctions",
    region_name=os.getenv("REGION_NAME"),
    aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
    aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
    endpoint_url=os.getenv("LOCALSTACK_ENDPOINT")  # If using LocalStack
))