class Vehicle:
    def __init__(self, model, capacity, vehicle_type, status, vehicle_id=None):
        self.vehicle_id = vehicle_id
        self.model = model
        self.capacity = capacity
        self.vehicle_type = vehicle_type
        self.status = status

    def __str__(self):
        return f"Vehicle(ID: {self.vehicle_id}, Model: {self.model}, Capacity: {self.capacity:.2f}, Type: {self.vehicle_type}, Status: {self.status})"
