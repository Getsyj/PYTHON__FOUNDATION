# Pyramid of Stars
for i in range(5):
    print(" " * (4 - i) + "*" * (2 * i + 1))

print()

# Pyramid of Alphabets
for i in range(1, 6):
    print(" " * (5 - i), end="")
    for j in range(65, 65 + i):
        print(chr(j), end=" ")
    print()

print()

# Pyramid of Numbers
for i in range(5):
    print(" " * (4 - i), end="")
    for j in range(1, 2 * i + 2):
        print(j, end="")
    print()

print()

# Inverted Pyramid of Stars
for i in range(5, 0, -1):
    print(" " * (5 - i) + "*" * (2 * i - 1))

print()

# Butterfly Pattern
n = 5
for i in range(1, n + 1):
    print("*" * i + " " * (2 * (n - i)) + "*" * i)
for i in range(n, 0, -1):
    print("*" * i + " " * (2 * (n - i)) + "*" * i)
