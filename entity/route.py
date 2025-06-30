class Route:
    def __init__(self, route_id, start_location, end_location, distance):
        self.route_id = route_id
        self.start_location = start_location
        self.end_location = end_location
        self.distance = distance

    def __str__(self):
        return f"Route(ID: {self.route_id}, From: {self.start_location}, To: {self.end_location}, Distance: {self.distance} km)"
