# Mastering Python - Lessons 033 to 036
# Topic: Booleans, Comparison, and Assignment Operators in Python
# This code covers key concepts from Lessons 33 to 36 of the "Mastering Python" course by Elzero Web School:
# - Lesson 033: Introduction to Boolean logic
# - Lesson 034: Advanced Boolean operations (and, or, not)
# - Lesson 035: Comparison operators for evaluating conditions
# - Lesson 036: Assignment operators for modifying variables

# Lesson 033 - Boolean Logic Part One
# Booleans represent True or False values
print("Boolean examples:")
print("True value:", True)
print("False value:", False)
print("Type of True:", type(True))
# Values that evaluate to False: 0, "", [], {}, None
print("Boolean of 0:", bool(0))
print("Boolean of '':", bool(""))
print("Boolean of []:", bool([]))
print("Boolean of non-empty string:", bool("Mohamed"))
print("Boolean of number:", bool(100))
print("")
print("------------------------------------")
print("")

# Lesson 034 - Boolean Logic Part Two
# Logical operators: and, or, not
name = "Mohamed"
age = 24
level = 10
print("Logical operators:")
# and: True if both conditions are True
print("name == 'Mohamed' and age >= 20:", name == "Mohamed" and age >= 20)
print("name == 'Mohamed' and age < 20:", name == "Mohamed" and age < 20)
# or: True if at least one condition is True
print("name == 'Mohamed' or age < 20:", name == "Mohamed" or age < 20)
print("name == 'Ali' or age < 20:", name == "Ali" or age < 20)
# not: Reverses the boolean value
print("not (age < 20):", not (age < 20))
print("Complex example:", not (name == "Ali" or age < 20))
print("")
print("------------------------------------")
print("")

# Lesson 035 - Comparison Operators
# Operators to compare values: ==, !=, >, <, >=, <=
a = 100
b = 200
print("Comparison operators:")
print("Equal (==):", a == b)
print("Not equal (!=):", a != b)
print("Greater than (>):", a > b)
print("Less than (<):", a < b)
print("Greater or equal (>=):", a >= b)
print("Less or equal (<=):", a <= b)
# Practical example
price = 150
budget = 200
print("Can buy? (price <= budget):", price <= budget)
print("")
print("------------------------------------")
print("")

# Lesson 036 - Assignment Operators
# Operators to assign and modify values: =, +=, -=, *=, /=, //=, **=
x = 10
y = 20
print("Assignment operators:")
print("Initial x:", x)
# Basic assignment
x = x + y
print("x = x + y:", x)  # 30
# Shorthand operators
x += y
print("x += y:", x)  # 50
x -= 10
print("x -= 10:", x)  # 40
x *= 5
print("x *= 5:", x)  # 200
x /= 100
print("x /= 100:", x)  # 2.0
x **= 2
print("x **= 2:", x)  # 4.0
x //= 3
print("x //= 3:", x)  # 1.0
print("")
print("------------------------------------")
print("")

# Summary of Lessons 033 to 036
print("Summary:")
print("1 - Learned Boolean values: True, False, and bool() conversion")
print("2 - Used logical operators: and, or, not for conditions")
print("3 - Applied comparison operators: ==, !=, >, <, etc.")
print("4 - Modified variables with assignment operators: +=, -=, *=, etc.")