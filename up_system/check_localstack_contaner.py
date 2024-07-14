import os
import yaml
import docker
from dotenv import load_dotenv
from utils import pdm
from enum import Enum

# Load environment variables from .env file
load_dotenv('.env')

class LocalstackMessages(Enum):
    CONTAINER_RUNNING = "Container '{container_name}' is running."
    CONTAINER_NOT_RUNNING = "Container '{container_name}' is not running (status: {status})."
    CONTAINER_NOT_FOUND = "Container '{container_name}' not found."
    API_ERROR = "Error checking container status: {error}"

class LocalstackManager:
    def __init__(self, compose_file='docker-compose.yml'):
        self.compose_file = compose_file
        self.client = docker.from_env()

    def read_docker_compose(self):
        """Read the docker-compose.yml file"""
        with open(self.compose_file, 'r') as file:
            return yaml.safe_load(file)

    def check_container_status(self, container_name):
        """Check the status of a Docker container"""
        try:
            container = self.client.containers.get(container_name)
            if container.status == 'running':
                pdm(LocalstackMessages.CONTAINER_RUNNING.value.format(container_name=container_name))
                print("Returning True")
                return True
            else:
                pdm(LocalstackMessages.CONTAINER_NOT_RUNNING.value.format(container_name=container_name, status=container.status))
                return False
        except docker.errors.NotFound:
            pdm(LocalstackMessages.CONTAINER_NOT_FOUND.value.format(container_name=container_name))
            return False
        except docker.errors.APIError as e:
            pdm(LocalstackMessages.API_ERROR.value.format(error=str(e)))
            return False

    def check_localstack(self):
        """Read Docker Compose configuration and check container status"""
        compose_config = self.read_docker_compose()
        container_name = compose_config['services']['localstack']['container_name']
        self.check_container_status(container_name)

if __name__ == "__main__":
    LocalstackManager().check_localstack()
