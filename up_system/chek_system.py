from utils import CheckSystem, RunningStatus
from enum import Enum
import docker
from check_localstack_contaner import LocalstackManager


if __name__=="__main__":


    def check_service(service_name: str, check_func) -> RunningStatus:
        try:
            check_func()
            return RunningStatus(True)
        except Exception as e:
            return RunningStatus(False, e, message=CheckSystem.EXC_MSG_DEFENSIVE_CODE_FOR_SERVICE.format(service_name))

    def check_docker() -> RunningStatus:
        return check_service("Docker",lambda: docker.from_env().ping())

    def check_localstack() -> RunningStatus:
        return check_service("Localstack", LocalstackManager().check_localstack)
        ## Err of s3 not exist-- lambda: requests.get("http://localhost:4566/health").raise_for_status())

    status = CheckSystem({
                "Docker": check_docker,
                "Localstack":check_localstack
                # Add more services here
            }).check_system()
    print(status)

