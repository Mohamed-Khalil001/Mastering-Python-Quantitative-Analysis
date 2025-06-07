# Mastering Python - Lessons 021 to 023
# Topic: Lists and Their Methods in Python
# This code covers key concepts from Lessons 21 to 23 of the "Mastering Python" course by Elzero Web School:
# - Lesson 021: Introduction to lists and basic methods
# - Lesson 022: More list methods for modification
# - Lesson 023: Advanced list methods for sorting and reversing

# Lesson 021 - List And Lists Methods Part One
# Lists are ordered, editable collections that can hold different data types
my_list = ["Mohamed", 24, 10.5, "Python", True]
print("Original list:", my_list)
print("Access first item:", my_list[0])  # Access by index (starts at 0)
print("Access last item:", my_list[-1])  # Negative index for end
print("Length of list:", len(my_list))  # Get number of items
# Append: add one item to the end
my_list.append("New Item")
print("After append('New Item'):", my_list)
# Add another list or item
numbers = [1, 2, 3]
my_list.append(numbers)
print("After append(numbers):", my_list)
print("Access nested list item:", my_list[-1][1])  # Access 2 from nested list
print("")
print("------------------------------------")
print("")

# Lesson 022 - Lists Methods Part Two
# More methods to modify lists
friends = ["Mohamed", "Ahmed", "Mahmoud"]
print("Original friends list:", friends)
# Extend: add items from another list/iterable
grades = ["A", "B", "C"]
friends.extend(grades)
print("After extend(grades):", friends)
# Remove: remove first occurrence of an item
friends.remove("Ahmed")
print("After remove('Ahmed'):", friends)
# Clear: remove all items
temp_list = [1, 2, 3, "Test"]
print("Temp list before clear:", temp_list)
temp_list.clear()
print("Temp list after clear:", temp_list)
print("")
print("------------------------------------")
print("")

# Lesson 023 - Lists Methods Part Three
# Methods for sorting, reversing, and copying
numbers = [5, 2, 8, 1, 9, 3]
print("Original numbers list:", numbers)
# Sort: arrange items in ascending order (works with same data type)
numbers.sort()
print("After sort():", numbers)
# Sort in descending order
numbers.sort(reverse=True)
print("After sort(reverse=True):", numbers)
# Reverse: flip the order of items (works with mixed types)
mixed = [1, "Python", 3.5, True]
print("Original mixed list:", mixed)
mixed.reverse()
print("After reverse():", mixed)
# Copy: create an independent copy of the list
original = [1, 2, 3, 4]
copy_list = original.copy()
print("Original list:", original)
print("Copied list:", copy_list)
original.append(5)
print("Original after append(5):", original)
print("Copied list unchanged:", copy_list)
print("")
print("------------------------------------")
print("")

# Summary of Lessons 021 to 023
print("Summary:")
print("1 - Created and accessed lists with append() and indexing")
print("2 - Modified lists with extend(), remove(), and clear()")
print("3 - Used sort(), reverse(), and copy() for advanced operations")