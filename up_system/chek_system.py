from utils import CheckSystem
from services_map import DOCKER_LOCALSTACK

def CheckDockerLocalstack():
    return CheckSystem(DOCKER_LOCALSTACK).check_system()

if __name__=="__main__":
    print(CheckDockerLocalstack())

