# Mastering Python - Lessons 017 to 018

# Topic: Strings Formatting in Python
# This code covers key concepts from Lessons 17 to 18 of the "Mastering Python" course by Elzero Web School:
# - Lesson 017: Strings formatting using old methods (% operator)
# - Lesson 018: Strings formatting using new methods (format() and f-strings)

# Lesson 017 - Strings Formatting Old Way
# Old formatting uses % operator for placeholders
name = "Mohamed"
age = 24
course = "Python"
# %s for strings, %d for integers, %f for floats
print("Old way formatting:")
print("Hello, %s! You are %d years old and learning %s." % (name, age, course))
# Control float precision with %.nf (n is number of decimal places)
price = 99.9999
print("Price: %.2f dollars" % price)  # Show 2 decimal places
# Multiple placeholders with different types
print("Student: %s, Age: %d, Score: %.1f" % (name, age, 95.555))
print("")
print("------------------------------------")
print("")

# Lesson 018 - Strings Formatting New Way
# Newer methods: format() and f-strings for cleaner, more readable formatting
# Using format() method
print("Using format() method:")
print("Hello, {}! You are {} years old and learning {}.".format(name, age, course))
# Specify order with indices
print("Student: {0}, Age: {1}, Course: {2}".format(name, age, course))
# Name placeholders for clarity
print("Student: {n}, Age: {a}, Course: {c}".format(n=name, a=age, c=course))
# Format float precision
print("Price: {:.2f} dollars".format(price))  # Show 2 decimal places
print("")
print("------------------------------------")
print("")

# Using f-strings (Python 3.6+)
print("Using f-strings (newest way):")
print(f"Hello, {name}! You are {age} years old and learning {course}.")
# Expressions inside f-strings
print(f"Next year, you will be {age + 1} years old.")
# Float precision in f-strings
print(f"Price: {price:.2f} dollars")
# Combine variables and text easily
print(f"Welcome, {name}! Your course '{course}' costs {price:.1f} dollars.")
print("")
print("------------------------------------")
print("")

# Summary of Lessons 017 to 018
print("Summary:")
print("1 - Formatted strings using old % operator (%s, %d, %f)")
print("2 - Used newer methods: format() for placeholders and f-strings for simplicity")
print("3 - Controlled float precision and combined variables with text")