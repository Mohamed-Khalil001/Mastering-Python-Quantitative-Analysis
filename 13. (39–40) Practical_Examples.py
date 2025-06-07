# Mastering Python - Lessons 039 to 040
# Topic: Practical Slicing and Real-World Applications in Python
# This code covers key concepts from Lessons 39 to 40 of the "Mastering Python" course by Elzero Web School:
# - Lesson 039: Practical training on slicing strings and lists
# - Lesson 040: Practical applications combining inputs, slicing, and calculations

# Lesson 039 - Practical Slicing Training
# Slicing extracts parts of strings, lists, or tuples using [start:end:step]
print("Slicing training:")
# String slicing
email = "mohamed@example.com"
print("Original email:", email)
print("Username (before '@'):", email[:email.index("@")])  # From start to @
print("Domain (after '@'):", email[email.index("@") + 1:])  # From after @ to end
print("First 3 chars:", email[:3])  # First 3 characters
print("Reverse email:", email[::-1])  # Reverse the string
# List slicing
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
print("Original list:", numbers)
print("First 4 items:", numbers[:4])  # From start to index 4 (not included)
print("Last 3 items:", numbers[-3:])  # Last 3 items
print("Every second item:", numbers[::2])  # Step by 2
print("Reverse list:", numbers[::-1])  # Reverse the list
print("")
print("------------------------------------")
print("")

# Lesson 040 - Practical Applications And Examples
# Combine inputs, slicing, and calculations for real-world tasks
# Example 1: Process user name
print("Example 1: Process user name")
fname = input("Enter your first name: ")
mname = input("Enter your middle name: ")
lname = input("Enter your last name: ")
# Clean and format inputs
fname = fname.strip().capitalize()
mname = mname.strip().capitalize()
lname = lname.strip().capitalize()
# Slice middle name to first letter
print(f"Hello, {fname} {mname[:1]}. {lname}! Welcome to our company!")
print("")
# Example 2: Calculate age in different units
print("Example 2: Age calculator")
age = int(input("Enter your age: "))
months = age * 12
weeks = months * 4
days = age * 365
hours = days * 24
print(f"You lived for:")
print(f"{months:,} months")
print(f"{weeks:,} weeks")
print(f"{days:,} days")
print(f"{hours:,} hours")
print("")
# Example 3: Extract email components
print("Example 3: Email breakdown")
email = input("Enter your email: ").strip()
username = email[:email.index("@")]
domain = email[email.index("@") + 1:]
print(f"Hello, {fname}! Your username is: {username}")
print(f"Your domain is: {domain}")
print("")
print("------------------------------------")
print("")

# Summary of Lessons 039 to 040
print("Summary:")
print("1 - Practiced slicing strings and lists with start, end, and step")
print("2 - Built practical apps: name formatting, age calculation, email breakdown")
print("3 - Combined input(), slicing, and calculations for real-world tasks")