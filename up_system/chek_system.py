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
        ## TODO : This is simple code, Exceptional hanling needed, Refer commit : 
        ##**1 e.g in https://github.com/nishant-firefly/aws/compare/861a107bd738bd428bb98a984d845701db890013...8d6d74459c180cc1961690318227113f627dc328
        ############ see the function check_docker 
        """TODO continues :  Before it was written like folowing and due to above check_Service exception handling is causing not handle exception properly
        def check_docker():
            try:
                client = docker.from_env()
                client.ping()
                return RunningStatus(True)
            except DockerException as e:
                return RunningStatus(False, e)
            except Exception as e:
                return RunningStatus(False, e, message="Defensive Coding, caught in generic exception")
        
        """
        return check_service("Docker",lambda: docker.from_env().ping())

    def check_localstack() -> RunningStatus:
        # TODO : Localstack is just returning True False, Exception handling needed e.g. above ##**1
        return check_service("Localstack", LocalstackManager().check_localstack)
        ## Err of s3 not exist-- lambda: requests.get("http://localhost:4566/health").raise_for_status())

    status = CheckSystem({
                "Docker": check_docker,
                "Localstack":check_localstack
                # Add more services here
            }).check_system()
    print(status)

