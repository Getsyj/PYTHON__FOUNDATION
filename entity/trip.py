
class Trip:
    def __init__(self, trip_id, vehicle_id, route_id, driver_id, departure_date, arrival_date, status):
        self.trip_id = trip_id
        self.vehicle_id = vehicle_id
        self.route_id = route_id
        self.driver_id = driver_id
        self.departure_date = departure_date
        self.arrival_date = arrival_date
        self.status = status

    def __str__(self):
        return f"Trip({self.trip_id}, Vehicle={self.vehicle_id}, Route={self.route_id}, Driver={self.driver_id}, Departure={self.departure_date}, Arrival={self.arrival_date}, Status={self.status})"
