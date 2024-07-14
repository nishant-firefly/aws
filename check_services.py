from up_system.utils import CheckSystem
from up_system.services_map import DOCKER_LOCALSTACK

if __name__=="__main__":
    status = CheckSystem(DOCKER_LOCALSTACK).check_system()
    print(status)