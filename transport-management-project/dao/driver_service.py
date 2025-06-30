from abc import ABC, abstractmethod
from entity.driver import Driver

class DriverService(ABC):

    @abstractmethod
    def add_driver(self, driver: Driver) -> bool:
        pass

    @abstractmethod
    def get_all_drivers(self) -> list[Driver]:
        pass

    @abstractmethod
    def get_available_drivers(self) -> list[Driver]:
        pass
