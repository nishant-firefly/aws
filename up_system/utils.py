import traceback
from enum import Enum
PRINT_PDM=False
def pdm(message: str, width: int = 20) -> None:
    if not PRINT_PDM: return 
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
        loc_dict=dict(self)
        if loc_dict['running']==True:
            # If status running do not show None messages, exceptions etc.
            return {k:v for k,v in loc_dict.items() if v}
        return loc_dict

    def __iter__(self):
        yield RunningStatus.RUNNING, self.running
        yield RunningStatus.EXCEPTION, self.exception
        yield RunningStatus.MESSAGE, self.message
        yield RunningStatus.TRACEBACK, self.traceback

class CheckSystem:
    EXC_MSG_DEFENSIVE_CODE_FOR_SERVICE= "Defensive Coding: caught in generic exception while checking {}"
    class ServiceStatusMessage(Enum):
        SERVICE_NOT_RUNNING = "{} is not running!"
        SERVICE_RUNNING = "{} is running!"

    def __init__(self, services_check_map) -> None:
        self.services_check_map=services_check_map

    def check_system(self) -> dict:
        statuses = {name: check() for name, check in self.services_check_map.items()}
        for service_name, status in statuses.items():
            if not status.running:
                pdm(CheckSystem.ServiceStatusMessage.SERVICE_NOT_RUNNING.value.format(service_name))
            else:
                pdm(CheckSystem.ServiceStatusMessage.SERVICE_RUNNING.value.format(service_name))
        return {service_name: status.to_dict() for service_name, status in statuses.items()}
    



