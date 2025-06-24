# Integer
a = 10
print(a, type(a))  # Output: 10 <class 'int'>

# Float
b = 3.14
print(b, type(b))  # Output: 3.14 <class 'float'>

# String
c = "Hello"
print(c, type(c))  # Output: Hello <class 'str'>

# Boolean
d = True
print(d, type(d))  # Output: True <class 'bool'>

# Complex
e = 2 + 3j
print(e, type(e))  # Output: (2+3j) <class 'complex'>

#Type casting 
# Casting float to int
x = 9.8
x_int = int(x)
print(x_int, type(x_int))  # 9 <class 'int'> (decimal part lost)

# Casting int to float
y = 7
y_float = float(y)
print(y_float, type(y_float))  # 7.0 <class 'float'>

# Casting number to string
z = 100
z_str = str(z)
print(z_str, type(z_str))  # '100' <class 'str'>

# Casting to boolean
print(bool(1))   # True (non-zero)
print(bool(0))   # False
print(bool(""))  # False (empty string)
print(bool("Hi"))# True (non-empty string)

paragraph = """Python is a powerful programming language.
It is easy to learn and widely used in web, AI, data science, and automation.
Python emphasizes readability and simplicity."""

# Length of the string
print("Length of string:", len(paragraph))

# Check for substrings
print("Is 'AI' in the paragraph?", "AI" in paragraph)
print("Is 'java' in the paragraph?", "java" in paragraph)

# Loop through characters
print("\nCharacters in the paragraph:")
for char in paragraph:
    print(char, end=" ")

str1 = "Virat kohli scored 200 in one day"

# Use find to locate and slice
start = str1.find("kohli")        # returns 6
end = start + len("kohli")        # 6 + 5 = 11
print(str1[start:end])            # Output: kohli

text = "PythonRocks"

print(text[0:6])
print(text[6:11])
print(text[2:5])
print(text[:6])
print(text[6:])

print(text[-5:])
print(text[-11:-5])
print(text[-9:-6])
print(text[-7:-2])
print(text[:-6])

myname = " bhavna, Panchariya, Joshi"

print(myname.upper())         # Converts all letters to uppercase
# Output: ' BHAVNA, PANCHARIYA, JOSHI'

print(myname.lower())         # Converts all letters to lowercase
# Output: ' bhavna, panchariya, joshi'

print(myname.strip())         # Removes leading and trailing spaces
# Output: 'bhavna, Panchariya, Joshi'

print(myname.replace("a","z"))# Replaces all occurrences of 'a' with 'z'
# Output: ' bhvznz, Pznchzriyz, Joshi'

print(myname.split(","))      # Splits the string at each comma into a list
# Output: [' bhavna', ' Panchariya', ' Joshi']

print(myname.count("a"))      # Counts how many times 'a' appears
# Output: 5

name = "Bhavna"
city = "Rajkot"
age = 22

formatted = f"My name is {name}, I live in {city}, and I am {age} years old."
print(formatted)

print(formatted.upper())
print(formatted.lower())
print(formatted.replace("Rajkot", "Ahmedabad"))
print(formatted.count("a"))
print(formatted.split(","))


single_quote = 'It\'s a test'
print(single_quote)

backslash = "backslash: \\"
print(backslash)

new_line = "Line1\nLine2"
print(new_line)

carriage_return = "Hello\rWorld"
print(carriage_return)

tab_space = "Name:\tGetsy"
print(tab_space)

backspace = "Helloo\b!"
print(backspace)

octal_value = "\110\145\154\154\157"
print(octal_value)

hex_value = "\x48\x65\x6C\x6C\x6F"
print(hex_value)



# Create a list
fruits = ["apple", "banana", "cherry", "mango"]
print(fruits)


print(fruits[2])

# Change item at index 1
fruits[1] = "orange"
print(fruits)

# Append using append()
fruits.append("grape")
print(fruits)

# Append multiple items using extend()
fruits.extend(["kiwi", "pineapple"])
print(fruits)

# Append using insert() at a specific index
fruits.insert(2, "guava")
print(fruits)

# Remove item using del (by index)
del fruits[0]
print(fruits)

# Remove item using remove() (by value)
fruits.remove("kiwi")
print(fruits)

# Remove all items using clear()
fruits.clear()
print(fruits)




# Create a list of squares from 1 to 5
squares = [x**2 for x in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]

# List of even numbers from 1 to 10
evens = [x for x in range(1, 11) if x % 2 == 0]
print(evens)  # [2, 4, 6, 8, 10]

# Convert all strings to uppercase
names = ["alice", "bob", "charlie"]
upper_names = [name.upper() for name in names]
print(upper_names)  # ['ALICE', 'BOB', 'CHARLIE']

# Define a tuple
mytup = (2, 1, 6, 4, 9, 6, False)

# Print the full tuple
print(mytup)

# Unpack the tuple into individual variables
(a, b, c, d, e, f, g) = mytup

# Print each element using the unpacked variables
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)

# Define another tuple
anothertup = (4, 6, 7)

# Print the second tuple
print(anothertup)


# Ask the user to enter age
age = int(input("Enter your age: "))

# Classify based on age
if age < 12:
    print("You are a Kid.")
elif age < 18:
    print("You are a Teen.")
elif age <= 60:
    print("You are an Adult.")
else:
    print("You are Old.")
