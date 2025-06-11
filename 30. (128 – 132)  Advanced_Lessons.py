# Mastering Python - Lessons 128 to 132
# Topic: Advanced Python Topics
# This code covers key concepts from Lessons 128 to 137 of the "Mastering Python" course by Elzero Web School:
# - Lesson 128: __name__ and __main__
# - Lesson 129: Timing your code with timeit
# - Lesson 130: Generate random serial numbers
# - Lesson 131: Unit testing with unittest
# - Lesson 132: NumPy introduction
# Lesson 133: Numpy Data Types And Attributes
# - Lesson 134: Numpy Array Creation Methods
# - Lesson 135: Numpy Array Reshaping
# - Lesson 136: Numpy Array Basic Operations
# - Lesson 137: Numpy Array Indexing & Slicing

import random
import string
import timeit
import unittest

# Lesson 128 - __name__ and __main__
# __name__ determines if a module is run directly or imported

print(f"__name__ and __main__: {__name__}")
if __name__ == "__main__":
    print("✔✅☪💯 PRINTED FROM DIRECT FILE ✔✅☪💯")
else:
    print("💙💙💙💙💙 PRINTED FROM IMPORTED FILE 💙💙💙💙💙")
print("This code runs regardless of __name__")
print("")
print("------------------------------------")
print("")

# Lesson 129 - Timing Your Code with timeit
# Measure code execution time for performance testing
print("Lesson 129 - Timing Your Code with timeit:")
def test_string_multiplication():
    name = "Mohamed"
    return name * 1000

# Time a single statement
print("Time for string multiplication (1M runs):",
      timeit.timeit("name='Mohamed'; name*1000", number=1000000))
# Time a random number generation
print("Time for random.randint (1M runs, repeated 4 times):",
      timeit.repeat(stmt="random.randint(0,50)", setup="import random", number=1000000, repeat=4))
# Time a function
print("Time for test_string_multiplication (1M runs):",
      timeit.timeit("test_string_multiplication()", setup="from __main__ import test_string_multiplication", number=1000000))
print("")
print("------------------------------------")
print("")

# Lesson 130 - Generate Random Serial Numbers
# Create random passwords or serial numbers
print("Lesson 130 - Generate Random Serial Numbers:")
def password_creator(count: int) -> str:
    """Generate a random password of specified length."""
    all_char = string.digits + string.ascii_lowercase + string.ascii_uppercase
    password_series = []
    for _ in range(count):
        pass_char = random.choice(all_char)
        password_series.append(pass_char)
    return "".join(password_series)

# Generate a 30-character password
print("Generated password (30 chars):", password_creator(30))
print("Generated password (10 chars):", password_creator(10))
print("")
print("------------------------------------")
print("")

# Lesson 131 - Unit Testing with unittest
# Write and run unit tests to verify code behavior
print("Lesson 131 - Unit Testing with unittest:")
class MyTest(unittest.TestCase):
    def test_greater_than(self):
        self.assertTrue(100 > 90, "100 should be greater than 90")
        # self.assertTrue(100 > 100, "This will fail")

    def test_equality(self):
        self.assertEqual(100, 100, "100 should equal 100")
        # self.assertEqual(100, 101, "This will fail")

    def test_password_length(self):
        result = password_creator(15)
        self.assertEqual(len(result), 15, "Password length should be 15")

if __name__ == "__main__":
    print("Running unit tests:")
    unittest.main(argv=[''], exit=False)  # Run tests without exiting
print("")
print("------------------------------------")
print("")

# Lesson 132 - NumPy Introduction
# Introduction to NumPy for numerical computations
print("Lesson 132 - NumPy Introduction:")
try:
    import numpy as np
except ImportError:
    print("NumPy not installed. Run 'pip install numpy' to use this lesson.")
    np = None

if np:
    print(f"Number of NumPy functions/classes: {len(dir(np))}")
    print("&" * 50)

    # List vs NumPy array
    my_list = [1, 2, 3, 4, 5]
    my_array = np.array(my_list)
    print("Python list:", my_list)
    print("NumPy array:", my_array)
    print("List type:", type(my_list))
    print("Array type:", type(my_array))
    print("&" * 50)

    # Accessing elements
    print("List[0]:", my_list[0])
    print("Array[0]:", my_array[0])
    print("&" * 50)

    # Array dimensions
    a = np.array(10)  # 0D
    b = np.array([10, 20])  # 1D
    c = np.array([[10, 20], [3, 4]])  # 2D
    d = np.array([[[1, 2], [2, 0]], [[33, 4], [3, 5]]])  # 3D
    print("0D array:", a)
    print("1D array:", b)
    print("2D array:\n", c)
    print("3D array:\n", d)
    print("Access d[0,1,0]:", d[0, 1, 0])
    print("&" * 50)

    # Custom dimensions
    my_custom_array = np.array([2, 3, 4], ndmin=3)
    print("Custom 3D array:\n", my_custom_array)
    print("Access [0,0,1]:", my_custom_array[0, 0, 1])
    print("&" * 50)

    # Memory comparison
    print("ID of list[0]:", id(my_list[0]))
    print("ID of list[1]:", id(my_list[1]))
    print("ID of array[0]:", id(my_array[0]))
    print("ID of array[1]:", id(my_array[1]))
    print("&" * 50)

    # Heterogeneous vs homogeneous
    my_list1 = [1, 2.3, "Hans", True]
    my_array1 = np.array([1, 2.3, "Hans", True])
    print("Heterogeneous list:", my_list1)
    print("Homogeneous array:", my_array1)
    print("Array dtype:", my_array1.dtype)

print("")
print("------------------------------------")
print("")

# Summary of Lessons 128 to 132
print("Summary:")
print("1 - Used __name__ == '__main__' to control code execution")
print("2 - Measured code performance with timeit")
print("3 - Generated random serial numbers with random and string")
print("4 - Wrote and ran unit tests with unittest")
print("5 - Introduced NumPy for efficient array operations")