import docker
from docker.errors import DockerException
import traceback

STRS = {
    "docker_not_running": "Docker is not running!",
    "docker_running": "Docker is running!",
}

def pdm(message: str, width: int = 20) -> None:
    border = '=' * width
    print(f"{border} {message.center(len(message) + 4)} {border}")

class RunningStatus:
    def __init__(self, running: bool, e: Exception = None, message: str = None) -> None:
        self.running = running
        self.exception = str(e) if e else None
        self.message = message
        self.traceback = traceback.format_exc() if e else None

    def __repr__(self) -> str:
        ## or can use self.__dict__ 
        return str(dict(self))

    def __str__(self) -> str:
        return str(dict(self))

    def to_dict(self) -> dict:
        return dict(self)

class CheckSystem:
    @staticmethod
    def check_docker() -> RunningStatus:
        try:
            client = docker.from_env()
            client.ping()
            return RunningStatus(True)
        except DockerException as e:
            return RunningStatus(False, e)
        except Exception as e:
            return RunningStatus(False, e, message="Defensive Coding: caught in generic exception")

    @staticmethod
    def check_system() -> RunningStatus:
        docker_status = CheckSystem.check_docker()
        if not docker_status.running:
            pdm(STRS["docker_not_running"])
            return docker_status
        pdm(STRS["docker_running"])
        return docker_status

if __name__ == "__main__":
    status = CheckSystem.check_system()
    breakpoint()
    print(str(status))
