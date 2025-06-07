# Mastering Python - Lessons 062 to 064
# Topic: Advanced Functions, Scope, Return, and Lambda in Python
# This code covers key concepts from Lessons 62 to 64 of the "Mastering Python" course by Elzero Web School:
# - Lesson 062: Global and function scope
# - Lesson 063: Difference between print and return in functions
# - Lesson 064: Lambda functions for inline operations

# Lesson 062 - Global and Function Scope
# Variables can have global or local scope
x = 2  # Global scope
print(f"Variable from global scope: {x}")

def scope():
    global x  # Modify global variable
    x = 10
    print(f"From function scope: {x}")

scope()
print(f"Variable from global scope after function update: {x}")

# Local scope example
def local_scope():
    y = 5  # Local scope
    print(f"From local scope: {y}")
local_scope()
# print(y)  # Error: y is not defined globally
print("")
print("------------------------------------")
print("")

# Lesson 063 - Return and Print in Functions
# Print displays output, return stores value
def test_print(x):
    print(x + 1)  # Displays but doesn't store
result = test_print(5)  # Prints 6
print(f"Result of test_print: {result}")  # None because no return

def test_return(x):
    return x + 1  # Stores value
result = test_return(5)  # No print, stores 6
print(f"Result of test_return: {result}")  # Prints 6

# Recursive function example
def clean_word(word):
    if len(word) < 2:
        return word
    if word[0] == word[1]:
        return clean_word(word[1:])
    return word[0] + clean_word(word[1:])
print("Recursive clean_word result:", clean_word("wwwoooorrld"))

# Another recursive example: sum numbers
def sum_numbers(n):
    if n <= 1:
        return n
    return n + sum_numbers(n - 1)
print("Sum numbers from 1 to 5:", sum_numbers(5))  # 15

# Recursive reverse word
def rev_word(word):
    if len(word) <= 1:
        return word
    return word[-1] + rev_word(word[:-1])
print("Reverse word 'hello':", rev_word("hello"))  # olleh
print("")
print("------------------------------------")
print("")

# Lesson 064 - Lambda Function
# Anonymous, single-line functions
def hello_name(name, age):
    return f"Hello {name}, your age is {age}"
nmag = lambda name, age: f"Hello {name}, your age is {age}"

print("Type of regular function:", type(hello_name))
print("Type of lambda function:", type(nmag))
print("Regular function:", hello_name("mohamed", 22))
print("Lambda function:", nmag("ahmed", 22))
print("Regular function name:", hello_name.__name__)
print("Lambda function name:", nmag.__name__)  # <lambda>

# Lambda in practical use
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print("Squared numbers using lambda:", squared)
print("")
print("------------------------------------")
print("")

# Summary of Lessons 062 to 064
print("Summary:")
print("1 - Learned global vs local scope and modifying global variables")
print("2 - Distinguished between print (display) and return (store) in functions")
print("3 - Used recursion for repetitive tasks like cleaning and reversing words")
print("4 - Created inline lambda functions for simple operations")