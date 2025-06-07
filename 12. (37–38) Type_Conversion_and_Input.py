# Mastering Python - Lessons 037 to 038
# Topic: Type Conversion and User Input in Python
# This code covers key concepts from Lessons 37 to 38 of the "Mastering Python" course by Elzero Web School:
# - Lesson 037: Converting between different data types
# - Lesson 038: Using the input() function to get user data

# Lesson 037 - Type Conversion
# Convert data types using built-in functions: int(), float(), str(), list(), tuple(), etc.
print("Type conversion examples:")
# Integer to other types
a = 10
print("Integer:", a, "Type:", type(a))
print("To float:", float(a), "Type:", type(float(a)))
print("To string:", str(a), "Type:", type(str(a)))
# Float to other types
b = 10.5
print("Float:", b, "Type:", type(b))
print("To integer:", int(b), "Type:", type(int(b)))  # Drops decimal part
print("To string:", str(b), "Type:", type(str(b)))
# String to other types
c = "123"
print("String:", c, "Type:", type(c))
print("To integer:", int(c), "Type:", type(int(c)))
print("To float:", float(c), "Type:", type(float(c)))
# List to tuple and vice versa
d = [1, 2, 3]
print("List:", d, "Type:", type(d))
print("To tuple:", tuple(d), "Type:", type(tuple(d)))
e = (4, 5, 6)
print("Tuple:", e, "Type:", type(e))
print("To list:", list(e), "Type:", type(list(e)))
print("")
print("------------------------------------")
print("")

# Lesson 038 - Input Function
# input() gets data from the user as a string
print("User input examples:")
name = input("Enter your name: ")
print("Hello,", name, "! Welcome!")
age = input("Enter your age: ")
print("Your age as string:", age, "Type:", type(age))
# Convert input to other types for calculations
age = int(age)  # Convert string to integer
print("Your age as integer:", age, "Type:", type(age))
# Practical example: calculate years until 30
years_to_30 = 30 - age
print("Years until you reach 30:", years_to_30)
# Handle float input
height = float(input("Enter your height in meters: "))
print("Your height in meters:", height, "Type:", type(height))
# Multiple inputs
city = input("Enter your city: ")
country = input("Enter your country: ")
print(f"You live in {city}, {country}!")
print("")
print("------------------------------------")
print("")

# Summary of Lessons 037 to 038
print("Summary:")
print("1 - Converted data types: int(), float(), str(), list(), tuple()")
print("2 - Used input() to get user data and converted it for use")
print("3 - Applied type conversion in practical examples")