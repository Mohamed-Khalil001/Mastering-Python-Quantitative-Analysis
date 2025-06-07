# Mastering Python - Lessons 009 to 011

# Topic: Strings, Escape Sequences, and Concatenation in Python
# This code covers key concepts from Lessons 9 to 11 of the "Mastering Python" course by Elzero Web School:
# - Lesson 009: Using escape sequences for special characters
# - Lesson 010: Concatenation and combining strings
# - Lesson 011: Introduction to strings and basic operations

# Lesson 009 - Escape Sequences Characters
# Escape sequences use backslash (\) to add special formatting or characters
print("Backspace example: hello\bworld")  # \b: Removes one character before
print("Escape new line: hello\
world")  # Escape new line continuation
print("Escape backslash: hello world\\")  # \\: Prints a backslash
print('Escape single quote: hello world\'from mohamed\'')  # \': Escapes single quote
print("Escape double quote: hello world \"from mohamed\"")  # \": Escapes double quote
print("Line feed:\nhello\nworld")  # \n: New line
print("Indented line feed:\nhello\n   world")  # \n with indentation
print("Long indent example:\nhello\n b              world")  # \n with spacing
print("Horizontal tab:\nhello\tworld")  # \t: Tab spacing
print("Hex value example:\n\x4D\x4F\x48")  # \xhh: Hex value (MOH = M, O, H)
print("")
print("------------------------------------")
print("")

# Lesson 010 - Concatenation And Training
# Concatenation: Combining strings using the + operator
print("Basic concatenation: hello " + "world")  # Combine two strings
mass = "hello"
agge = "world"
print("Variable concatenation:", mass + " " + agge)  # Add space between variables
full = mass + "\n" + agge
print("Concatenation with new line:", full)
# Note: You can only concatenate strings, not strings and other types
# print("hello " + 1)  # Error: uncomment to test
print("")
print("------------------------------------")
print("")

# Lesson 011 - Strings
# Strings are text data, enclosed in single ('') or double ("") quotes
greeting = "Hello, Python!"
name = 'Mohamed'
print("String examples:")
print("Greeting:", greeting)
print("Name:", name)
# Strings are immutable (can't change individual characters)
# greeting[0] = 'h'  # Error: strings can't be modified directly
print("Length of greeting:", len(greeting))  # Get string length
print("First character:", greeting[0])  # Access first character
print("Last character:", greeting[-1])  # Access last character
print("")
print("------------------------------------")
print("")

# Summary of Lessons 009 to 011
print("Summary:")
print("1 - Used escape sequences for formatting (e.g., \\, \n, \t)")
print("2 - Learned to concatenate strings with + operator")
print("3 - Explored strings: creation, length, and basic indexing")