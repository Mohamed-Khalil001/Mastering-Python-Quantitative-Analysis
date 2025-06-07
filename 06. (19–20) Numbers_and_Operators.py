# Mastering Python - Lessons 019 to 020
# Topic: Numbers and Basic Operators in Python
# This code covers key concepts from Lessons 19 to 20 of the "Mastering Python" course by Elzero Web School:
# - Lesson 019: Understanding numbers and their types
# - Lesson 020: Using operators with numbers for calculations

# Lesson 019 - Numbers
# Python supports three main number types: integers, floats, and complex
print("Integer (whole number):", 10)  # Integer: no decimal point
print("Type of 10:", type(10))
print("Float (decimal number):", 10.5)  # Float: has decimal point
print("Type of 10.5:", type(10.5))
print("Complex number:", 3 + 4j)  # Complex: real + imaginary part (j)
print("Type of 3 + 4j:", type(3 + 4j))
# Convert between types
num = 15
print("Convert int to float:", float(num))  # Integer to float
print("Convert float to int:", int(10.9))  # Float to int (removes decimal)
print("")
print("------------------------------------")
print("")

# Lesson 020 - Operators And Numbers Training
# Arithmetic operators for calculations
a = 10
b = 3
print("Basic arithmetic operators:")
print("Addition (+):", a + b)  # Add: 10 + 3
print("Subtraction (-):", a - b)  # Subtract: 10 - 3
print("Multiplication (*):", a * b)  # Multiply: 10 * 3
print("Division (/):", a / b)  # Divide: 10 / 3 (returns float)
print("Floor division (//):", a // b)  # Divide, round down to integer
print("Modulus (%):", a % b)  # Remainder of division: 10 % 3
print("Exponent (**):", a ** b)  # Power: 10 raised to 3
print("")
# Practical examples
price = 100
discount = 20
tax = 5
final_price = price - discount + tax
print("Practical example: Calculate final price")
print("Original price:", price)
print("Discount:", discount)
print("Tax:", tax)
print("Final price (price - discount + tax):", final_price)
print("")
print("------------------------------------")
print("")

# Summary of Lessons 019 to 020
print("Summary:")
print("1 - Learned number types: integer, float, and complex")
print("2 - Used arithmetic operators: +, -, *, /, //, %, **")
print("3 - Applied operators in practical calculations")