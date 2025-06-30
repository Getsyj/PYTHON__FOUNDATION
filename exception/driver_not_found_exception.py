class DriverNotFoundException(Exception):
    def __init__(self, driver_id: int):
        super().__init__(f"Driver with ID {driver_id} not found.")
