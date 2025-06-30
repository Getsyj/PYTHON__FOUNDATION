from abc import ABC, abstractmethod
from typing import List

from entity.trip import Trip
from entity.booking import Booking


class TripService(ABC):
 
    @abstractmethod
    def schedule_trip(self, trip: Trip) -> bool:
        """Insert a new trip into the database."""
        pass

    @abstractmethod
    def cancel_trip(self, trip_id: int) -> bool:
        """Mark a trip as cancelled (or delete, depending on rules)."""
        pass

    @abstractmethod
    def allocate_driver_to_trip(self, trip_id: int, driver_id: int) -> bool:
        """Assign a driver to a specific trip."""
        pass

    @abstractmethod
    def deallocate_driver(self, trip_id: int) -> bool:
        """Remove the driver assignment from a trip."""
        pass


    @abstractmethod
    def get_all_trips(self) -> List[Trip]:
        """Return a list of all trips (for 'View All Trips')."""
        pass

    @abstractmethod
    def get_bookings_by_trip(self, trip_id: int) -> List[Booking]:
        """Return all bookings linked to the specified trip."""
        pass
