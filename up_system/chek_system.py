from check_localstack_contaner import LocalstackManager
from utils import CheckSystem

if __name__=="__main__":
    status = CheckSystem({
                "Docker": LocalstackManager().check_docker,
                "Localstack":LocalstackManager().check_localstack
                # Add more services here
            }).check_system()
    print(status)

