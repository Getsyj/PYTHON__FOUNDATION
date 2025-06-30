from abc import ABC, abstractmethod
from entity.passenger import Passenger

class PassengerService(ABC):

    @abstractmethod
    def add_passenger(self, passenger: Passenger) -> bool:
        pass

    @abstractmethod
    def get_all_passengers(self) -> list[Passenger]:
        pass
