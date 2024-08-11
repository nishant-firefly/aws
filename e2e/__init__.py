import os 
from dotenv import load_dotenv
import boto3
from enum import Enum
class ENVS(Enum):
    SERVICES="SERVICES"
    REGION_NAME="REGION_NAME"
    AWS_ACCESS_KEY_ID="AWS_ACCESS_KEY_ID"
    AWS_SECRET_ACCESS_KEY="AWS_SECRET_ACCESS_KEY"
    LOCALSTACK_ENDPOINT="LOCALSTACK_ENDPOINT"

class SERVICES(Enum):
    S3="s3"
    IAM="iam" 
    STEPFUNCTIONS="stepfunctions" 
    LAMBDA="lambda"
    DYNAMODB="dynamodb"

dotenv_path = os.path.join(os.path.dirname(__file__), '..', 'up_system', '.env')
load_dotenv(dotenv_path)
clients = {}
for service in [e.strip() for e in os.getenv(ENVS.SERVICES.value).split(",")]:
    # Using getattr to ensure service is from services only 
    clients[getattr(SERVICES,service.upper()).value] =boto3.client(service,
    region_name=os.getenv(ENVS.REGION_NAME.value),
    aws_access_key_id=os.getenv(ENVS.AWS_ACCESS_KEY_ID.value),
    aws_secret_access_key=os.getenv(ENVS.AWS_SECRET_ACCESS_KEY.value),
    endpoint_url=os.getenv(ENVS.LOCALSTACK_ENDPOINT.value)  # If using LocalStack
)
print(clients)