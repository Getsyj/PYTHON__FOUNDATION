class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name                    # Public
        self._roll_number = roll_number     # Protected
        self.__marks = marks                # Private

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Roll Number: {self._roll_number}")
        print(f"Marks: {self.__marks}")

    def _update_roll_number(self, new_roll):
        self._roll_number = new_roll
        print(f"Updated Roll Number (Protected): {self._roll_number}")

    def __update_marks(self, new_marks):
        self.__marks = new_marks
        print(f"Updated Marks (Private): {self.__marks}")

    def access_private_method(self, new_marks):
        self.__update_marks(new_marks)
s = Student("Alice", 101, 95)
s.display_details()
s._update_roll_number(202)
s.access_private_method(88)
s.display_details()

# Creating object
s = Student("Alice", 101, 95)

# Modify and print public attribute
s.name = "Alicia"
print("Modified Name (Public):", s.name)

# Modify and print protected attribute
s._roll_number = 202
print("Modified Roll Number (Protected):", s._roll_number)

# Try to access private attribute directly
try:
    print("Attempting to access __marks directly:", s.__marks)
except AttributeError as e:
    print("Error accessing __marks directly:", e)

# Display full details using class method
s.display_details()

class Topper(Student):
    def __init__(self, name, roll_number, marks):
        super().__init__(name, roll_number, marks)

    def try_access(self):
        print("Accessing Protected Attribute from Subclass:", self._roll_number)

        try:
            print("Trying to access Private Attribute from Subclass:", self.__marks)
        except AttributeError as e:
            print("Error accessing __marks from subclass:", e)
# Create Topper object and call method
t = Topper("Bob", 301, 99)
t.try_access()
# Access private __marks using name mangling
print("Accessing __marks using name mangling:", s._Student__marks)

# Update private __marks using name mangling
s._Student__marks = 88
print("Modified __marks using name mangling:", s._Student__marks)

# Confirm with display method
s.display_details()
