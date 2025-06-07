# Mastering Python - Lessons 026 to 029
# Topic: Sets and Their Methods in Python
# This code covers key concepts from Lessons 26 to 29 of the "Mastering Python" course by Elzero Web School:
# - Lesson 026: Introduction to sets and basic properties
# - Lesson 027: Basic set methods for adding and removing
# - Lesson 028: Set methods for combining sets
# - Lesson 029: Advanced set methods for comparison

# Lesson 026 - Set And Methods Part One
# Sets are unordered, unique collections; only immutable types allowed (no lists or dicts)
my_set = {1, 2, "Mohamed", 3, "Python"}
print("Original set:", my_set)
# Sets remove duplicates automatically
duplicates = {1, 2, 2, 3, 3, "Test", "Test"}
print("Set with duplicates removed:", duplicates)
# No indexing or slicing because sets are unordered
# print(my_set[0])  # Error: uncomment to test
# Only immutable types: numbers, strings, tuples
valid_set = {1, "Hello", (2, 3)}
print("Valid set with mixed types:", valid_set)
# Invalid: lists and dicts are unhashable
# invalid_set = {1, [2, 3]}  # Error: uncomment to test
print("")
print("------------------------------------")
print("")

# Lesson 027 - Set Methods Part Two
# Methods to add and remove items from sets
my_set = {1, 2, 3, 4}
print("Original set:", my_set)
# add(): add one item
my_set.add(5)
print("After add(5):", my_set)
# remove(): remove item, raises error if not found
my_set.remove(3)
print("After remove(3):", my_set)
# discard(): remove item, no error if not found
my_set.discard(10)  # No error even if 10 isn't in set
print("After discard(10):", my_set)
# pop(): remove and return a random item
popped = my_set.pop()
print("Popped item:", popped)
print("Set after pop():", my_set)
print("")
print("------------------------------------")
print("")

# Lesson 028 - Set Methods Part Three
# Methods to combine and modify sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print("Set 1:", set1)
print("Set 2:", set2)
# union(): combine sets, keep unique items
union_set = set1.union(set2)
print("Union of set1 and set2:", union_set)
# update(): add items from another set/iterable to set1
set1.update({7, 8})
print("Set1 after update({7, 8}):", set1)
# intersection(): get common items
common = set1.intersection(set2)
print("Intersection of set1 and set2:", common)
# intersection_update(): update set1 to keep only common items
set1.intersection_update(set2)
print("Set1 after intersection_update(set2):", set1)
print("")
print("------------------------------------")
print("")

# Lesson 029 - Set Methods Part Four
# Advanced methods for set comparison
set_a = {1, 2, 3, 4, 5}
set_b = {1, 2, 3}
set_c = {6, 7, 8}
print("Set A:", set_a)
print("Set B:", set_b)
print("Set C:", set_c)
# difference(): items in set_a but not in set_b
diff = set_a.difference(set_b)
print("Difference (set_a - set_b):", diff)
# difference_update(): update set_a to remove items in set_b
set_a.difference_update(set_b)
print("Set A after difference_update(set_b):", set_a)
# symmetric_difference(): items in either set, but not both
sym_diff = set_a.symmetric_difference(set_b)
print("Symmetric difference of set_a and set_b:", sym_diff)
# issuperset(), issubset(), isdisjoint()
print("Is set_b a subset of set_a?:", set_b.issubset(set_a))
print("Is set_a a superset of set_b?:", set_a.issuperset(set_b))
print("Are set_a and set_c disjoint?:", set_a.isdisjoint(set_c))  # No common items
print("")
print("------------------------------------")
print("")

# Summary of Lessons 026 to 029
print("Summary:")
print("1 - Learned set properties: unordered, unique, immutable types only")
print("2 - Used add(), remove(), discard(), and pop() to modify sets")
print("3 - Combined sets with union(), update(), and intersection()")
print("4 - Compared sets with difference(), issubset(), issuperset(), etc.")