from abc import ABC, abstractmethod
from entity.booking import Booking

class BookingService(ABC):

    @abstractmethod
    def add_booking(self, booking: Booking) -> bool:
        pass

    @abstractmethod
    def get_all_bookings(self) -> list[Booking]:
        pass
