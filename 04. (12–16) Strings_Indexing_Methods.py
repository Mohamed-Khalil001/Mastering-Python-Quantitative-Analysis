# Mastering Python - Lessons 012 to 016
# Topic: Strings - Indexing, Slicing, and Common Methods
# This code covers key concepts from Lessons 12 to 16 of the "Mastering Python" course by Elzero Web School:
# - Lesson 012: Indexing and slicing strings
# - Lesson 013: Strings methods part one (basic methods)
# - Lesson 014: Strings methods part two (formatting methods)
# - Lesson 015: Strings methods part three (search and replace)
# - Lesson 016: Strings methods part four (advanced methods)

# Lesson 012 - Strings - Indexing And Slicing
# Strings are ordered; use indexing to access characters and slicing to get substrings
greeting = "Hello, Python!"
print("Original string:", greeting)
print("First character (index 0):", greeting[0])  # Index starts at 0
print("Last character (index -1):", greeting[-1])  # Negative index from end
print("Slice from 0 to 5:", greeting[0:5])  # Slice: 'Hello' (5 not included)
print("Slice from 7 to end:", greeting[7:])  # From index 7 to end
print("Slice with step:", greeting[0:12:2])  # Step by 2: 'Hlo y'
print("Reverse string:", greeting[::-1])  # Reverse with step -1
print("")
print("------------------------------------")
print("")

# Lesson 013 - Strings Methods Part One
# Basic string methods for manipulation
name = "  mohamed  "
print("Original with spaces:", name)
print("strip():", name.strip())  # Remove leading/trailing spaces
print("upper():", name.upper())  # Convert to uppercase
print("lower():", name.lower())  # Convert to lowercase
print("capitalize():", "mohamed is learning".capitalize())  # Capitalize first letter
print("title():", "mohamed is learning python".title())  # Capitalize each word
print("")
print("------------------------------------")
print("")

# Lesson 014 - Strings Methods Part Two
# More string methods for formatting and counting
text = "Hello, hello, Python!"
print("Original text:", text)
print("count('l'):", text.count("l"))  # Count occurrences of 'l'
print("count('hello'):", text.count("hello"))  # Count occurrences of 'hello'
print("center(20, '*'):", text.center(20, "*"))  # Center text, pad with *
print("ljust(20, '-'):", text.ljust(20, "-"))  # Left justify, pad with -
print("rjust(20, '-'):", text.rjust(20, "-"))  # Right justify, pad with -
print("")
print("------------------------------------")
print("")

# Lesson 015 - Strings Methods Part Three
# String methods for searching and replacing
message = "Hello, Python Learners!"
print("Original message:", message)
print("find('Python'):", message.find("Python"))  # Find index of 'Python'
print("find('Java'):", message.find("Java"))  # Returns -1 if not found
print("index('Python'):", message.index("Python"))  # Find index, errors if not found
# print("index('Java'):", message.index("Java"))  # Error: uncomment to test
print("replace('Python', 'World'):", message.replace("Python", "World"))  # Replace text
print("replace('l', 'L', 2):", message.replace("l", "L", 2))  # Replace first 2 'l'
print("")
print("------------------------------------")
print("")

# Lesson 016 - Strings Methods Part Four
# Advanced string methods for checking properties
code = "Python3.9"
email = "mohamed@example.com"
print("Original strings:", code, email)
print("isalpha():", code.isalpha())  # Check if all characters are letters
print("isalnum():", code.isalnum())  # Check if all characters are letters or numbers
print("isdigit():", "123".isdigit())  # Check if all characters are digits
print("isspace():", "   ".isspace())  # Check if all characters are spaces
print("startswith('Py'):", code.startswith("Py"))  # Check if starts with 'Py'
print("endswith('.com'):", email.endswith(".com"))  # Check if ends with '.com'
print("")
print("------------------------------------")
print("")

# Summary of Lessons 012 to 016
print("Summary:")
print("1 - Used indexing and slicing to access string parts")
print("2 - Applied basic methods: strip(), upper(), lower(), etc.")
print("3 - Used formatting methods: count(), center(), ljust(), etc.")
print("4 - Explored search/replace: find(), index(), replace()")
print("5 - Checked string properties: isalpha(), isalnum(), startswith(), etc.")