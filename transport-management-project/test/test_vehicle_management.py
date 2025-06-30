import unittest
from dao.trip_impl import TripServiceImpl

class TestDriverMapping(unittest.TestCase):

    def setUp(self):
        self.trip_service = TripServiceImpl()

    def test_allocate_driver_to_trip(self):
        
        trip_id = 1  
        driver_id = 1  
        result = self.trip_service.allocate_driver_to_trip(trip_id, driver_id)
        self.assertTrue(result, f"Failed to allocate driver {driver_id} to trip {trip_id}")

    def test_deallocate_driver_from_trip(self):
        trip_id = 1  
        result = self.trip_service.deallocate_driver(trip_id)
        self.assertTrue(result, f"Failed to deallocate driver from trip {trip_id}")

if __name__ == '__main__':
    unittest.main()
