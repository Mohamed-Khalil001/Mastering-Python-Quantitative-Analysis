# Mastering Python - Lessons 001 to 005
# Topic: Introduction and Basics
# This code covers key concepts from Lessons 001 to 005 of the "Mastering Python" course by Elzero Web School:
# - Lesson 001: Introduction to Python
# - Lesson 002: First Python program
# - Lesson 003: Comments
# - Lesson 004: Reserved words
# - Lesson 005: Print function basics

# # # _________________________________Lesson 001 _______________________
# # # --Introduction => What is Python --
# # # ----------------------------------------------
# # # Python is a high-level, interpreted programming language
# # # Created by Guido van Rossum, first released in 1991
# # # Used for web development, data science, automation, and more
# # # Easy to read and write due to simple syntax
# # # ----------------------------------------------
import keyword
print("Lesson 001 - Introduction to Python:")
print("Python is a versatile programming language")
print("Created by Guido van Rossum in 1991")
print("Applications: Web, Data Science, Automation")
print("")
print("------------------------------------")
print("")

# # # _________________________________Lesson 002 _______________________
# # # --First Program => Hello World --
# # # ----------------------------------------------
# # # Write your first Python program
# # # Use print() to display output
# # # ----------------------------------------------
print("Lesson 002 - First Python Program:")
print("Hello, World!")
print("")
print("------------------------------------")
print("")

# # # _________________________________Lesson 003 _______________________
# # # --Comments => Single and Multi-line --
# # # ----------------------------------------------
# # # Comments explain code, ignored by interpreter
# # # Single-line: # Comment
# # # Multi-line: """ Comment """
# # # ----------------------------------------------
print("Lesson 003 - Comments:")
# This is a single-line comment
print("Code with comments:")
"""
This is a multi-line comment
It can span multiple lines
"""
print("Comments are not executed")
print("")
print("------------------------------------")
print("")

# # # _________________________________Lesson 004 _______________________
# # # -- Reserved Words --
# # # Reserved words are keywords with special meaning in Python
# # # Examples: if, for, while, print, return
# # # # ----------------------------------------------
print("Lesson 004 - Reserved Words:")
print("Reserved words in Python:")
print(keyword.kwlist)
print("Example: 'if' is reserved, can't be used as variable name")
# if = 5  # This will raise a syntax error
print("")
print("------------------------------------")
print("")

# # # _________________________________Lesson 005 _______________________
# # # --Print => Basics --
# # # ----------------------------------------------
# # # print() outputs text to the console
# # # Can use sep and end parameters
# # # ----------------------------------------------
print("Lesson 005 - Print Function Basics:")
print("Hello", "Python", sep=" - ", end="!")
print(" Next line")
print("Multiple arguments:", 1, 2, 3)
print("")
print("------------------------------------")
print("")

# Summary of Lessons 001 to 005
print("Summary:")
print("1 - Introduced Python and its applications")
print("2 - Wrote first Hello World program")
print("3 - Learned single and multi-line comments")
print("4 - Explored reserved words")
print("5 - Used print() with sep and end parameters")
