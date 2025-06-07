# Mastering Python - Lessons 024 to 025
# Topic: Tuples and Their Methods in Python
# This code covers key concepts from Lessons 24 to 25 of the "Mastering Python" course by Elzero Web School:
# - Lesson 024: Introduction to tuples and basic properties
# - Lesson 025: Tuple methods and operations

# Lesson 024 - Tuple And Methods Part One
# Tuples are ordered, immutable collections that can hold different data types
# Use parentheses () or no parentheses for creation
tuple1 = ("Mohamed", 24, 10.5, "Python")
tuple2 = "Ahmed", 23, True  # No parentheses works too
print("Tuple with parentheses:", tuple1)
print("Tuple without parentheses:", tuple2)
print("Type of tuple1:", type(tuple1))
print("Type of tuple2:", type(tuple2))
# Access items by index (ordered)
print("First item of tuple1:", tuple1[0])
print("Last item of tuple1:", tuple1[-1])
# Tuples are immutable: can't change items
# tuple1[0] = "Ali"  # Error: uncomment to test
print("Length of tuple1:", len(tuple1))  # Get number of items
# Single-element tuple needs a comma
single = ("Mohamed",)
not_tuple = ("Mohamed")
print("Single-element tuple:", single, "Type:", type(single))
print("Not a tuple:", not_tuple, "Type:", type(not_tuple))
print("")
print("------------------------------------")
print("")

# Lesson 025 - Tuple Methods Part Two
# Tuples have limited methods due to immutability
my_tuple = ("Ahmed", 23, "Python", 23, True)
print("Original tuple:", my_tuple)
# count(): count occurrences of an item
print("Count of 23 in tuple:", my_tuple.count(23))  # Counts how many times 23 appears
# index(): find first index of an item
print("Index of 'Python' in tuple:", my_tuple.index("Python"))  # First occurrence
# Concatenation: combine tuples with +
tuple3 = (1, 2, 3)
tuple4 = ("A", "B", "C")
combined = tuple3 + tuple4
print("Concatenated tuples:", combined)
# Repetition: repeat tuple with *
print("Repeat tuple3 three times:", tuple3 * 3)
# Tuple destructuring: assign items to variables
a, b, c = tuple3
print("Destructuring tuple3:")
print("a:", a)
print("b:", b)
print("c:", c)
# Use underscore (_) for ignored values
x, y, _, z = ("Mohamed", 24, "Python", True)
print("Destructuring with ignore:")
print("x:", x)
print("y:", y)
print("z:", z)
print("")
print("------------------------------------")
print("")

# Summary of Lessons 024 to 025
print("Summary:")
print("1 - Learned tuple properties: ordered, immutable, allows mixed types")
print("2 - Used tuple methods: count(), index(), and operations like + and *")
print("3 - Applied destructuring to assign tuple items to variables")