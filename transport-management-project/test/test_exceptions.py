import unittest
from dao.transport_impl import TransportServiceImpl
from exception.vehicle_not_found_exception import VehicleNotFoundException
from exception.booking_not_found_exception import BookingNotFoundException

class TestExceptionHandling(unittest.TestCase):
    def setUp(self):
        self.service = TransportServiceImpl()

    def test_vehicle_not_found_exception(self):
        result = self.service.delete_vehicle(99999)  
        self.assertFalse(result, "Expected VehicleNotFoundException to be handled")

    def test_booking_not_found_exception(self):
        result = self.service.cancel_booking(99999) 
        self.assertFalse(result, "Expected BookingNotFoundException to be handled")

class DriverNotFoundException(Exception):
    def __init__(self, driver_id: int):
        super().__init__(f"Driver with ID {driver_id} not found.")

class TripNotFoundException(Exception):
    def __init__(self, trip_id: int):
        super().__init__(f"Trip with ID {trip_id} not found.")

class PassengerNotFoundException(Exception):
    def __init__(self, passenger_id: int):
        super().__init__(f"Passenger with ID {passenger_id} not found.")
