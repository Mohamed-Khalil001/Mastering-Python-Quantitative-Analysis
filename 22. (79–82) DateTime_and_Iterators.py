# Mastering Python - Lessons 079 to 082
# Topic: DateTime, Iterables, Iterators, and Generators in Python
# This code covers key concepts from Lessons 79 to 82 of the "Mastering Python" course by Elzero Web School:
# - Lesson 079: Working with date and time
# - Lesson 080: Formatting date and time
# - Lesson 081: Understanding iterables and iterators
# - Lesson 082: Creating generators with yield

import datetime
try:
    import termcolor
except ModuleNotFoundError:
    print("termcolor not installed. Run: pip install termcolor for colored output")

# Lesson 079 - Date and Time
# Using datetime module to handle dates and times
print("Lesson 079 - Date and Time:")
print("Module classes:", dir(datetime))
print("-" * 60)
print("datetime class methods:", dir(datetime.datetime))
print("-" * 60)

# Current date and time
print("Current date and time:", datetime.datetime.now())
print("Current year:", datetime.datetime.now().year)
print("Current month:", datetime.datetime.now().month)
print("Current day:", datetime.datetime.now().day)
print("-" * 60)

# Min and max dates
print("Min date:", datetime.datetime.min)
print("Max date:", datetime.datetime.max)
print("-" * 60)

# Current time components
print("Current time:", datetime.datetime.now().time())
print("Current hour:", datetime.datetime.now().time().hour)
print("Current minute:", datetime.datetime.now().time().minute)
print("Current second:", datetime.datetime.now().time().second)
print("-" * 60)

# Min and max times
print("Min time:", datetime.time.min)
print("Max time:", datetime.time.max)
print("-" * 60)

# Specific date and age calculation
my_birthday = datetime.datetime(2001, 4, 2)
date_now = datetime.datetime.now()
print("Specific date (2001-04-02):", my_birthday)
print(f"You lived for {(date_now - my_birthday).days} days")
print("")
print("------------------------------------")
print("")

# Lesson 080 - Date and Time Formatting
# Formatting dates using strftime
print("Lesson 080 - Date and Time Formatting:")
my_birthday = datetime.datetime(2001, 2, 4)
print("Full weekday name:", my_birthday.strftime("%A"))
print("Short weekday name:", my_birthday.strftime("%a"))
print("Full month name:", my_birthday.strftime("%B"))
print("Short month name:", my_birthday.strftime("%b"))
print("Custom format:", my_birthday.strftime("%d - %b - %Y"))
print("")
print("------------------------------------")
print("")

# Lesson 081 - Iterable vs Iterator
# Iterables can be looped over; iterators use next()
print("Lesson 081 - Iterable vs Iterator:")
my_name = "Mohamed"
print("Looping over iterable (string):")
for char in my_name:
    print(char, end=" ")
print()

my_list = [1, 3, 20, 39, 4]
print("Looping over iterable (list):")
for num in my_list:
    print(num, end=" ")
print()

# Convert iterable to iterator
my_iterator = iter(my_list)
print("Using iterator with next():")
print(next(my_iterator))  # 1
print(next(my_iterator))  # 3
print(next(my_iterator))  # 20
print("Looping over remaining iterator items:")
for num in my_iterator:
    print(num, end=" ")
print()
print("Looping over iterable directly with iter():")
for num in iter(my_list):
    print(num, end=" ")
print()
print("")
print("------------------------------------")
print("")

# Lesson 082 - Generators
# Functions with yield create generator iterators
print("Lesson 082 - Generators:")


def my_generator():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5


print("Generator object:", my_generator())
my_gen = my_generator()
print("Using next() with generator:")
print(next(my_gen))  # 1
print("...continuing...")
print(next(my_gen))  # 2
print("...continuing...")
print(next(my_gen))  # 3
print("Looping over remaining generator items:")
for n in my_gen:
    print(n)
print("")
print("------------------------------------")
print("")

# Summary of Lessons 079 to 082
print("Summary:")
print("1 - Handled dates and times with datetime module")
print("2 - Formatted dates using strftime")
print("3 - Distinguished between iterables and iterators using for and next()")
print("4 - Created generators with yield for lazy evaluation")
