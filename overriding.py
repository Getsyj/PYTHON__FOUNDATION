class Box:
    def __init__(self, volume):
        self.volume = volume

    # Overload '+' operator
    def __add__(self, other):
        return Box(self.volume + other.volume)

    # Overload '-' operator
    def __sub__(self, other):
        return Box(self.volume - other.volume)

    # Overload '*' operator
    def __mul__(self, other):
        return Box(self.volume * other.volume)

    # Overload '==' operator
    def __eq__(self, other):
        return self.volume == other.volume

    # For printing
    def __str__(self):
        return f"Box Volume: {self.volume}"


# Create Box objects
b1 = Box(10)
b2 = Box(5)
b3 = Box(10)

# + operator
add_result = b1 + b2
print("Addition:", add_result)  # Box Volume: 15

# - operator
sub_result = b1 - b2
print("Subtraction:", sub_result)  # Box Volume: 5

# * operator
mul_result = b1 * b2
print("Multiplication:", mul_result)  # Box Volume: 50

# == operator
print("Equality (b1 == b3):", b1 == b3)  # True
print("Equality (b1 == b2):", b1 == b2)  # False
