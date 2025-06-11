# Mastering Python - Lessons 093 to 094
# Topic: Debugging and Type Hinting in Python
# This code covers key concepts from Lessons 93 to 94 of the "Mastering Python" course by Elzero Web School:
# - Lesson 093: Debugging techniques to find and fix errors
# - Lesson 094: Using type hints to specify expected data types

import pdb

# Lesson 093 - Debugging
# Debugging involves identifying and fixing errors using tools like print, pdb, or IDE debuggers
print("Lesson 093 - Debugging:")
# Example: Debugging a function with potential errors


def calculate_average(numbers):
    """Calculate the average of a list of numbers."""
    # Adding print statements for debugging
    print(f"Input numbers: {numbers}")
    if not numbers:
        print("Debug: Empty list detected")
        return 0
    total = sum(numbers)
    print(f"Debug: Sum calculated: {total}")
    count = len(numbers)
    print(f"Debug: Count of numbers: {count}")
    average = total / count
    print(f"Debug: Average calculated: {average}")
    return average


# Test with potential issues
numbers = [10, 20, 30, "40"]  # Contains a string to cause an error
try:
    print("Result:", calculate_average(numbers))
except TypeError as e:
    print(f"Error caught: {e}")
    print("Debugging tip: Check if all elements are numbers")

# Using pdb for interactive debugging
print("\nUsing pdb for interactive debugging:")


def divide_numbers(a, b):
    """Divide two numbers."""
    pdb.set_trace()  # Start debugging here
    result = a / b
    return result

# Test pdb (uncomment to run interactively)
# print(divide_numbers(10, 0))  # Will pause at pdb.set_trace()


print("")
print("------------------------------------")
print("")

# Lesson 094 - Type Hinting
# Using type hints to specify expected types
print("Lesson 094 - Type Hinting:")


def hello(name: str) -> str:
    """Greets the user with a welcome message.

    Args:
        name (str): The name to greet

    Returns:
        str: The greeting message
    """
    return f"Hello {name}, you are welcome!"


# Valid usage
print("Valid usage:", hello("Mohamed"))
# Invalid usage (no error, but type hint for clarity)
print("Invalid usage (no error):", hello(10))


def add(a: int, b: int) -> int:
    """Adds two numbers.

    Args:
        a (int): First number
        b (int): Second number

    Returns:
        int: Sum of a and b
    """
    return a + b


print("Add integers:", add(2, 3))  # 5
print("Add strings (unexpected):", add("2", "3"))  # "23"
print("")
print("------------------------------------")
print("")

# Summary of Lessons 093 to 094
print("Summary:")
print("1 - Demonstrated debugging with print statements and pdb")
print("2 - Introduced type hinting for function parameters and return types")
