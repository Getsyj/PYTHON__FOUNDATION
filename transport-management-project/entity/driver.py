class Driver:
    def __init__(self, driver_id, name, license_number, status):
        self.driver_id = driver_id
        self.name = name
        self.license_number = license_number
        self.status = status

    def __str__(self):
        return (
            f"Driver(ID: {self.driver_id}, Name: {self.name}, "
            f"License: {self.license_number}, Status: {self.status})"
        )
