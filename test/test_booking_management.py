

import unittest
from dao.transport_impl import TransportServiceImpl

class TestBookingManagement(unittest.TestCase):
    def setUp(self):
        self.transport_service = TransportServiceImpl()

    def test_book_trip_success(self):
     
        trip_id = 1
        passenger_id = 1
        booking_date = "2025-06-25"

        result = self.transport_service.book_trip(trip_id, passenger_id, booking_date)
        self.assertTrue(result, f"❌ Booking failed for passenger {passenger_id} on trip {trip_id}")
