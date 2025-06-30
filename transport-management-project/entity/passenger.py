class Passenger:
    def __init__(self, passenger_id, first_name, age, gender, email, phone_number):
        self.passenger_id = passenger_id
        self.first_name = first_name
        self.age = age
        self.gender = gender
        self.email = email
        self.phone_number = phone_number

    def __str__(self):
        return (
            f"Passenger(ID: {self.passenger_id}, Name: {self.first_name}, "
            f"Age: {self.age}, Gender: {self.gender}, Email: {self.email}, Phone: {self.phone_number})"
        )