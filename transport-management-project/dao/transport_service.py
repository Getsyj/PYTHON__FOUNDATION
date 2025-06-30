from abc import ABC, abstractmethod
from entity.vehicle import Vehicle
from entity.booking import Booking
from entity.driver import Driver

class TransportService(ABC):

    @abstractmethod
    def add_vehicle(self, vehicle: Vehicle) -> bool:
        pass

    @abstractmethod
    def update_vehicle(self, vehicle: Vehicle) -> bool:
        pass

    @abstractmethod
    def delete_vehicle(self, vehicle_id: int) -> bool:
        pass

    @abstractmethod
    def get_all_vehicles(self) -> list[Vehicle]:
        pass

    @abstractmethod
    def book_trip(self, trip_id: int, passenger_id: int, booking_date: str) -> bool:
        """
        Books a trip for a passenger.
        Returns True if successful, False otherwise.
        """
        pass

    @abstractmethod
    def cancel_booking(self, booking_id: int) -> bool:
        """
        Cancels a booking by setting its status to 'Cancelled'.
        Returns True if successful, False otherwise.
        """
        pass

    @abstractmethod
    def get_bookings_by_passenger(self, passenger_id: int) -> list[Booking]:
        """
        Retrieves all bookings made by a specific passenger.
        """
        pass

    @abstractmethod
    def get_bookings_by_trip(self, trip_id: int) -> list[Booking]:
        """
        Retrieves all bookings for a specific trip.
        """
        pass

    @abstractmethod
    def get_available_drivers(self) -> list[Driver]:
        """
        Retrieves a list of available drivers not allocated to any trip.
        """
        pass
