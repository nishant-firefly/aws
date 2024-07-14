import yaml
import os
import docker
from dotenv import load_dotenv
from utils import pdm
from enum import Enum
from utils import RunningStatus
from enum import Enum
import docker
from docker.errors import DockerException
from __init__ import parent_dir 

# Load environment variables from .env file
load_dotenv('.env')

class LocalstackMessages(Enum):
    CONTAINER_RUNNING = "Container '{container_name}' is running."
    CONTAINER_NOT_RUNNING = "Container '{container_name}' is not running (status: {status})."
    CONTAINER_NOT_FOUND = "Container '{container_name}' not found."
    API_ERROR = "Error checking container status: {error}"

class LocalstackManager:
    def __init__(self, compose_file_name='docker-compose.yml'):
        self.compose_file = os.path.join(parent_dir, compose_file_name)
        self.client = docker.from_env()

    def read_docker_compose(self):
        """Read the docker-compose.yml file"""
        with open(self.compose_file, 'r') as file:
            return yaml.safe_load(file)

    def check_container_status(self, container_name) -> RunningStatus:
        """Check the status of a Docker container"""
        try:
            container = self.client.containers.get(container_name)
            if container.status == 'running':
                pdm(LocalstackMessages.CONTAINER_RUNNING.value.format(container_name=container_name))
                return RunningStatus(True)
            else:
                msg=LocalstackMessages.CONTAINER_NOT_RUNNING.value.format(container_name=container_name, status=container.status)
                pdm(msg)
                return RunningStatus(True, message=msg)
        except docker.errors.NotFound as e:
            pdm(LocalstackMessages.CONTAINER_NOT_FOUND.value.format(container_name=container_name))
            return RunningStatus(False,e)
        except docker.errors.APIError as e:
            pdm(LocalstackMessages.API_ERROR.value.format(error=str(e)))
            return RunningStatus(False,e)
        
    def check_docker(self) -> RunningStatus:
        ## TODO : This is simple code, Exceptional hanling needed, Refer commit : 
        ##**1 e.g in https://github.com/nishant-firefly/aws/compare/861a107bd738bd428bb98a984d845701db890013...8d6d74459c180cc1961690318227113f627dc328
        ############ see the function check_docker 
        try:
            client = docker.from_env()
            client.ping()
            return RunningStatus(True)
        except DockerException as e:
            return RunningStatus(False, e)
        except Exception as e:
            return RunningStatus(False, e, message="Defensive Coding, caught in generic exception")

    def check_localstack(self) -> RunningStatus:
        """Read Docker Compose configuration and check container status"""
        # TODO: Handle following 2 lines if issue
        compose_config = self.read_docker_compose()
        container_name = compose_config['services']['localstack']['container_name']
        return self.check_container_status(container_name)

if __name__ == "__main__":
    LocalstackManager().check_localstack()
