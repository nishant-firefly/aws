from utils import CheckSystem, RunningStatus
from enum import Enum
import docker
from check_localstack_contaner import LocalstackManager


if __name__=="__main__":
    class Service(Enum):
        DOCKER = "Docker"
        LOCALSTACK = "Localstack"

        # Add more services here as needed
    class ServiceChecks:
        @staticmethod
        def docker() -> RunningStatus:
            return CheckSystem.check_service(Service.DOCKER, lambda: docker.from_env().ping())

        @staticmethod
        def localstack() -> RunningStatus:
            return CheckSystem.check_service(Service.LOCALSTACK, LocalstackManager().check_localstack())
            # lambda: requests.get("http://localhost:4566/health").raise_for_status())
    SERVICES_CHECK_MAP ={
                Service.DOCKER.value: ServiceChecks.docker,
                Service.LOCALSTACK.value:ServiceChecks.localstack
                # Add more services here
            }
    status = CheckSystem(SERVICES_CHECK_MAP).check_system()
    print(status)

