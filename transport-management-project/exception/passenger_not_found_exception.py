class PassengerNotFoundException(Exception):
    def __init__(self, passenger_id: int):
        super().__init__(f"Passenger with ID {passenger_id} not found.")
