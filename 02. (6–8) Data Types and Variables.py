# Mastering Python - Lessons 006 to 008
# Topic: Data Types and Variables in Python
# This code covers key concepts from Lessons 6 to 8 of the "Mastering Python" course by Elzero Web School:
# - Lesson 006: Overview of basic data types in Python
# - Lesson 007: Introduction to variables and naming rules
# - Lesson 008: More on variables: multiple assignment and best practices

# Lesson 006 - Some Data Types Overview
# Python has several built-in data types for storing different kinds of data
print("String: hello")  # String (str) - for text
print("Type of 'hello':", type("hello"))
print("Integer: 10")  # Integer (int) - for whole numbers
print("Type of 10:", type(10))
print("Float: 10.5")  # Float - for decimal numbers
print("Type of 10.5:", type(10.5))
print("List: [1, 2, 3]")  # List - for ordered, editable collections
print("Type of [1, 2, 3]:", type([1, 2, 3]))
print("Tuple: (1, 2, 3)")  # Tuple - for ordered, non-editable collections
print("Type of (1, 2, 3):", type((1, 2, 3)))
print("Dictionary: {'key': 'value'}")  # Dictionary - for key-value pairs
print("Type of {'key': 'value'}:", type({"key": "value"}))
print("Boolean: True")  # Boolean - for True/False values
print("Type of True:", type(True))
print("")
print("------------------------------------")
print("")

# Lesson 007 - Variables Part One
# Variables store data; follow these naming rules:
# - Case-sensitive (Name and name are different)
# - Can't start with numbers or special characters (except underscore)
# - Use meaningful names for clarity
_name = "mohamed"  # Valid: starts with underscore
name = "mohamed"  # Normal naming
firstName = "mohamed"  # camelCase
first_name = "mohamed"  # snake_case (preferred in Python)
print("Variables with different naming styles:")
print("Underscore start:", _name)
print("Normal:", name)
print("camelCase:", firstName)
print("snake_case:", first_name)
# Note: Invalid names (uncomment to test errors)
# 1name = "mohamed"  # Error: can't start with number
# name@ = "mohamed"  # Error: can't use special characters
print("")
print("------------------------------------")
print("")

# Lesson 008 - Variables Part Two
# Multiple assignment: assign values to multiple variables at once
a, s, d = 1, 3, 4
print("Multiple assignment:")
print("a:", a)
print("s:", s)
print("d:", d)
# Best practices:
# - Use descriptive names (e.g., 'age' instead of 'a')
# - Avoid reserved words (e.g., 'print', 'type')
age, height, name = 24, 1.75, "mohamed"
print("Better variable names:")
print("Age:", age)
print("Height:", height)
print("Name:", name)
print("")
print("------------------------------------")
print("")

# Summary of Lessons 006 to 008
print("Summary:")
print("1 - Explored basic data types: string, int, float, list, tuple, dict, bool")
print("2 - Learned to create variables with naming rules")
print("3 - Used multiple assignment and best practices for variables")