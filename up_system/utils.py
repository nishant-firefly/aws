import traceback
from enum import Enum
from abc import abstractmethod, ABC
from __init__ import pdm

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
class Service(ABC):
    @abstractmethod
    def check(self) -> RunningStatus:
        pass
class CheckService:
    
    EXC_MSG_DEFENSIVE_CODE_FOR_SERVICE= "Defensive Coding: caught in generic exception while checking {}"

    def __init__(self, SERVICES_LIST) -> None:
        # TODO: Move out and resolve cyclic import error.
        from services_map import SERVICES_MAP
        self.services_check_map={k:v for k,v in SERVICES_MAP.items() if k in SERVICES_LIST}


    class ServiceStatusMessage(Enum):
        SERVICE_NOT_RUNNING = "{} is not running!"
        SERVICE_RUNNING = "{} is running!"

    def check_service(self) -> dict:

        statuses = {name: getattr(service_class(),'check')() for name, service_class in self.services_check_map.items()}
        for service_name, status in statuses.items():
            if not status.running:
                pdm(CheckService.ServiceStatusMessage.SERVICE_NOT_RUNNING.value.format(service_name))
            else:
                pdm(CheckService.ServiceStatusMessage.SERVICE_RUNNING.value.format(service_name))
        return {service_name: status.to_dict() for service_name, status in statuses.items()}

    



