import docker
from docker.errors import DockerException
import traceback

RUNNING, EXCEPTION, MESSAGE = "running", "exception", "message"

def print_decorated_message(message):
    # Calculate the length of the message for centering
    message_length = len(message)
    
    # Print the styled message
    print(f"{'=' * 20} {message.center(message_length + 4)} {'=' * 20}")
class RunningStatus:
    def __init__(self, running: bool, e: Exception = None, message: str = None) -> None:
        self.running = running
        self.exception = e
        self.message = message
        self.traceback_str = traceback.format_exc() if e else None
        self.json = {
            RUNNING: running,
            "exception": str(e) if e else None,
            "message": message,
            "traceback_str": self.traceback_str
        }

    def __repr__(self) -> str:
        """
        Purpose: The __repr__ method is intended to provide a "formal" string representation of an object that can be used to recreate the object when passed to the eval() function. It is primarily used for debugging and development.
        Usage: The goal of __repr__ is to be unambiguous and to provide as much information as possible about the object.
        """
        return str(self.json)

    def __str__(self) -> str:
        return str({
            RUNNING: self.running,
            EXCEPTION: self.exception,
            MESSAGE: self.message
        })

    def to_dict(self) -> dict:
        return self.json

def check_docker():
    try:
        client = docker.from_env()
        client.ping()
        return RunningStatus(True)
    except DockerException as e:
        return RunningStatus(False, e)
    except Exception as e:
        return RunningStatus(False, e, message="Defensive Coding, caught in generic exception")

def check_system():
    docker_status=check_docker()
    if not docker_status.running:
        return docker_status
    print_decorated_message("Docker is running !")
    breakpoint()



if __name__ == "__main__":
    status=check_system()
    print("*************************************")
    print(str(status)) # By default. If repr overrides
    print("====================================")
    # print(repr(status))
    """
    when both __repr__ and __str__ methods are defined in a class, the __str__ method gets priority over __repr__ when you use the str() 
    function or the print() statement. This means that if both methods are defined, str(obj) and print(obj) 
    will call the __str__ method, while repr(obj) will call the __repr__ method.
    """