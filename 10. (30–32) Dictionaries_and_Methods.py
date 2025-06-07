# Mastering Python - Lessons 030 to 032
# Topic: Dictionaries and Their Methods in Python
# This code covers key concepts from Lessons 30 to 32 of the "Mastering Python" course by Elzero Web School:
# - Lesson 030: Introduction to dictionaries and basic properties
# - Lesson 031: Basic dictionary methods for modification
# - Lesson 032: Advanced dictionary methods and operations

# Lesson 030 - Dictionary And Methods Part One
# Dictionaries store key-value pairs; keys must be unique and immutable
student = {
    "name": "Mohamed",
    "age": 24,
    "course": "Python",
    "grade": 95.5
}
print("Original dictionary:", student)
# Access values by key
print("Name:", student["name"])
# Keys can be strings, numbers, or tuples (immutable types)
mixed = {
    "name": "Ahmed",
    1: "ID",
    ("skill", "level"): "Expert"
}
print("Dictionary with mixed keys:", mixed)
# Access keys and values
print("All keys:", student.keys())
print("All values:", student.values())
# Note: Keys must be unique; duplicates overwrite
duplicate = {"name": "Mohamed", "name": "Ali"}
print("Dictionary with duplicate keys:", duplicate)  # Last value wins
print("")
print("------------------------------------")
print("")

# Lesson 031 - Dictionary Methods Part Two
# Methods to modify dictionaries
profile = {
    "name": "Mohamed",
    "age": 24,
    "course": "Python"
}
print("Original profile:", profile)
# clear(): remove all items
profile.clear()
print("After clear():", profile)
# Rebuild for next examples
profile = {
    "name": "Mohamed",
    "age": 24,
    "course": "Python"
}
# update(): add or update key-value pairs
profile.update({"grade": 95, "level": "Beginner"})
print("After update():", profile)
# pop(): remove a key and return its value
popped = profile.pop("age")
print("Popped 'age':", popped)
print("Profile after pop():", profile)
print("")
print("------------------------------------")
print("")

# Lesson 032 - Dictionary Methods Part Three
# Advanced methods and operations
data = {
    "name": "Mohamed",
    "skill": "Python",
    "rating": 4.5
}
print("Original data:", data)
# setdefault(): get value or add key with default if not found
print("Get 'name':", data.setdefault("name", "Unknown"))
print("Add 'city' if missing:", data.setdefault("city", "Cairo"))
print("Data after setdefault():", data)
# items(): return list of key-value pairs (tuples)
print("All items:", data.items())
# fromkeys(): create dictionary from keys with a default value
keys = ("a", "b", "c")
default_value = "Unknown"
new_dict = dict.fromkeys(keys, default_value)
print("New dict from fromkeys():", new_dict)
# popitem(): remove and return last key-value pair
last_item = data.popitem()
print("Popped last item:", last_item)
print("Data after popitem():", data)
print("")
print("------------------------------------")
print("")

# Summary of Lessons 030 to 032
print("Summary:")
print("1 - Learned dictionary properties: key-value pairs, unique keys")
print("2 - Modified dicts with clear(), update(), and pop()")
print("3 - Used advanced methods: setdefault(), items(), fromkeys(), popitem()")