# Mastering Python - Lessons 088 to 092
# Topic: Docstrings, Code Linting, and Exception Handling in Python
# This code covers key concepts from Lessons 88 to 92 of the "Mastering Python" course by Elzero Web School:
# - Lesson 088: Commenting vs documenting with docstrings
# - Lesson 089: Using Pylint for code quality
# - Lesson 090: Raising custom exceptions
# - Lesson 091: Basic exception handling with try/except/else/finally
# - Lesson 092: Advanced exception handling with file access example

# Lesson 088 - Commenting vs Documenting
# Docstrings provide function/module documentation
def operation(n1: int, n2: int) -> None:
    """This is a summation function.

    Args:
        n1 (int): First number
        n2 (int): Second number

    Returns:
        None: Prints the sum of n1 and n2
    """
    print(n1 + n2)


def hello(name: str) -> None:
    """Prints a greeting message.

    Args:
        name (str): Name to greet
    """
    print(f"Hello {name}")


print("Lesson 088 - Commenting vs Documenting:")
print("Operation docstring:", operation.__doc__)
operation(5, 3)
print("Hello help:")
help(hello)
hello("World")
print("")
print("------------------------------------")
print("")

# Lesson 089 - Installing and Using Pylint
# Pylint checks code quality (run: pip install pylint)
"""
This module demonstrates a simple greeting function for Pylint compliance.
"""


def greet(name: str) -> None:
    """Greets the user with a message.

    Args:
        name (str): The name to greet
    """
    print(f"Hello {name}")


print("Lesson 089 - Pylint for Better Code:")
greet("Ahmed")
print("Run 'pylint 088_Docstrings_and_Errors.py' in terminal to check code quality.")
print("")
print("------------------------------------")
print("")

# Lesson 090 - Errors and Exceptions Raising
# Raising custom exceptions with raise
print("Lesson 090 - Raising Exceptions:")
# Syntax error example (uncomment to test)
# print "Osama"  # SyntaxError

x = -10
print("Without raising exception:")
if x < 0:
    print(f"{x} is negative")
else:
    print(f"{x * 100 / 100:.0f}")

# Raise custom exception
try:
    y = -10
    if y < 0:
        print(f"{y} is negative")
    else:
        raise ValueError(f"{y} is negative")
except ValueError as e:
    print(f"Error: {e}")
print("Continuing execution...")
print("Hello")
print("")
print("------------------------------------")
print("")

# Lesson 091 - Exception Handling
# Try/except/else/finally for error handling
print("Lesson 091 - Basic Exception Handling:")
try:
    number = int(input("Enter an integer: "))
except ValueError:
    print("Input is not an integer!")
else:
    print(f"{number + 10}: We added 10 to your number")
finally:
    print("All is done 🐺🐱‍🐉👾👽")

# Specific exception handling
try:
    # print(10 / 0)  # ZeroDivisionError
    # print(z)  # NameError
    print(int("Hello"))  # ValueError
except ZeroDivisionError:
    print("Cannot divide by zero")
except NameError:
    print("Variable not defined")
except ValueError:
    print("Invalid value")
print("")
print("------------------------------------")
print("")

# Lesson 092 - Advanced Exception Handling
# File access with limited tries
print("Lesson 092 - Advanced Exception Handling:")
the_file = None
tries = 5
while tries > 0:
    try:
        user_file = input(
            "Enter file path (e.g., C:\\Users\\space\\Downloads\\file.txt): ").strip()
        the_file = open(user_file, "r")
        print("\n😂😁 Good! File content:\n", the_file.read())
        break
    except FileNotFoundError:
        tries -= 1
        print(f"You have {tries} tries left! 🐱‍👓")
    except Exception as e:
        print(f"Error occurred: {e}")
    finally:
        if the_file is not None:
            the_file.close()
            print("\n\nDONE: File read and closed 🦮🦮")
else:
    print("Your tries are done 😪😱🤬")
print("")
print("------------------------------------")
print("")


# Summary of Lessons 088 to 092
print("Summary:")
print("1 - Used docstrings for function/module documentation")
print("2 - Demonstrated Pylint for code quality checks")
print("3 - Raised custom exceptions with raise")
print("4 - Handled errors with try/except/else/finally")
print("5 - Built an advanced file access example with limited tries")
