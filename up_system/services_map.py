from check_localstack_contaner import LocalstackManager
from enum import Enum
class ServiceConst(Enum):
    Docker="Docker"
    Localstack="Localstack"

SERVICES_MAP={
                ServiceConst.Docker.value: LocalstackManager().check_docker,
                ServiceConst.Localstack.value:LocalstackManager().check_localstack
                # Add more services here
}
DOCKER_LOCALSTACK=[
    ServiceConst.Docker.value, 
    ServiceConst.Localstack.value, 
]