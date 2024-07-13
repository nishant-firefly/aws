import docker
from docker.errors import DockerException
import traceback
from enum import Enum



def pdm(message: str, width: int = 20) -> None:
    border = '=' * width
    print(f"{border} {message.center(len(message) + 4)} {border}")

class RunningStatus:
    RUNNING, EXCEPTION, MESSAGE, TRACEBACK = "running", "exception", "message", "traceback"

    def __init__(self, running: bool, e: Exception = None, message: str = None) -> None:
        self.running = running
        self.exception = str(e) if e else None
        self.message = message
        self.traceback = traceback.format_exc() if e else None

    def __repr__(self) -> str:
        return str(dict(self))

    def __str__(self) -> str:
        return str(dict(self))

    def to_dict(self) -> dict:
        return dict(self)

    def __iter__(self):
        yield RunningStatus.RUNNING, self.running
        yield RunningStatus.EXCEPTION, self.exception
        yield RunningStatus.MESSAGE, self.message
        yield RunningStatus.TRACEBACK, self.traceback
class Service(Enum):
    DOCKER = "Docker"
    LOCALSTACK = "Localstack"

    # Add more services here as needed
class CheckSystem:

    class ServiceStatusMessage(Enum):
        SERVICE_NOT_RUNNING = "{} is not running!"
        SERVICE_RUNNING = "{} is running!"

    EXC_MSG_DEFENSIVE_CODE_FOR_SERVICE= "Defensive Coding: caught in generic exception while checking {}"

    @staticmethod
    def check_service(service_name: str, check_func) -> RunningStatus:
        try:
            check_func()
            return RunningStatus(True)
        except Exception as e:
            return RunningStatus(False, e, message=CheckSystem.EXC_MSG_DEFENSIVE_CODE_FOR_SERVICE.format(service_name))

    @staticmethod
    def check_docker() -> RunningStatus:
        return CheckSystem.check_service(Service.DOCKER, lambda: docker.from_env().ping())

    @staticmethod
    def check_local_stack() -> RunningStatus:
        return CheckSystem.check_service(Service.LOCALSTACK, False)

    @staticmethod
    def check_system() -> dict:
        services = {
            Service.DOCKER.value: CheckSystem.check_docker,
            Service.LOCALSTACK.value:CheckSystem.check_local_stack
            # Add more services here
        }

        statuses = {name: check() for name, check in services.items()}

        for service_name, status in statuses.items():
            if not status.running:
                pdm(CheckSystem.ServiceStatusMessage.SERVICE_NOT_RUNNING.value.format(service_name))
            else:
                pdm(CheckSystem.ServiceStatusMessage.SERVICE_RUNNING.value.format(service_name))

        return {service_name: status.to_dict() for service_name, status in statuses.items()}

if __name__ == "__main__":
    status = CheckSystem.check_system()
    print(status)
