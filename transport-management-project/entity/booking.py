class Booking:
    def __init__(self, booking_id, trip_id, passenger_id, booking_date, status):
        self.booking_id = booking_id
        self.trip_id = trip_id
        self.passenger_id = passenger_id
        self.booking_date = booking_date
        self.status = status

    def __str__(self):
        return (
            f"Booking(ID: {self.booking_id}, TripID: {self.trip_id}, PassengerID: {self.passenger_id}, "
            f"Date: {self.booking_date}, Status: {self.status})"
        )
