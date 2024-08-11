breakpoint()
from varni.utils.aws.env_clients import get_aws_service_clients
import os 
from dotenv import load_dotenv
dotenv_path = os.path.join(os.path.dirname(__file__), '..', 'up_system', '.env')
load_dotenv(dotenv_path)
AWS_SERVICE_CLIENTS= get_aws_service_clients()
print(AWS_SERVICE_CLIENTS)