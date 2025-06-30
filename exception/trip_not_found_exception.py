class TripNotFoundException(Exception):
    def __init__(self, trip_id: int):
        super().__init__(f"Trip with ID {trip_id} not found.")
