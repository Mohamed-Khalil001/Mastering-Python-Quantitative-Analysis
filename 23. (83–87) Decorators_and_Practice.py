# Mastering Python - Lessons 083 to 087
# Topic: Decorators, Zip Function, and Image Manipulation in Python
# This code covers key concepts from Lessons 83 to 87 of the "Mastering Python" course by Elzero Web School:
# - Lesson 083: Introduction to decorators
# - Lesson 084: Advanced decorators with parameters
# - Lesson 085: Practical decorator for speed testing
# - Lesson 086: Zip function for combining iterables
# - Lesson 087: Image manipulation with Pillow

from time import time
try:
    import termcolor
except ModuleNotFoundError:
    print("termcolor not installed. Run: pip install termcolor for colored output")
try:
    from PIL import Image
except ModuleNotFoundError:
    print("Pillow not installed. Run: pip install Pillow for image manipulation")

# Lesson 083 - Decorator Introduction
# Decorators enhance functions by wrapping them


def my_decorate(fun):
    def wrapper():
        try:
            print(termcolor.colored("************** Start *************", "yellow"))
        except NameError:
            print("************** Start *************")
        fun()
        try:
            print(termcolor.colored("************** End ***************", "yellow"))
        except NameError:
            print("************** End ***************")
    return wrapper


@my_decorate
def say_hello():
    print("Hello Mohamed")


say_hello()
print("")
print("------------------------------------")
print("")

# Lesson 084 - Advanced Decorators
# Decorators with parameters and multiple layers


def my_decorate_2(fun):
    def wrapper(num1, num2):
        print("--- I am from decorate_2 ---")
        fun(num1, num2)
    return wrapper


def my_decorate(fun):
    def wrapper(num1, num2):
        try:
            print(termcolor.colored("************** Start *************", "yellow"))
        except NameError:
            print("************** Start *************")
        if num1 < 0 or num2 < 0:
            try:
                print(termcolor.colored(
                    "!! Be Aware: One or more numbers are negative", "red"))
            except NameError:
                print("!! Be Aware: one or more numbers are negative")
        fun(num1, num2)
        try:
            print(termcolor.colored("************** End ***************", "yellow"))
        except NameError:
            print("************** End ***************")
    return wrapper


@my_decorate
@my_decorate_2
def sum_cap(num1, num2):
    print(f"Sum: {num1 + num2}")


sum_cap(-1, 100)
print("")
print("------------------------------------")
print("")

# Lesson 085 - Practical Decorator (Speed Test)
# Decorator to measure function execution time


def speed_test_decorator(fun):
    def wrapper(*numbers):
        try:
            print(termcolor.colored("************** Start *************", "yellow"))
        except NameError:
            print("************** Start *************")
        for number in numbers:
            if number < 0:
                try:
                    print(termcolor.colored(
                        "!! Be Aware: One or more numbers are negative", "red"))
                except NameError:
                    print("!! Be Aware: one or more numbers are negative")
        start = time()
        fun(*numbers)
        end = time()
        print(f"Time taken: {end - start:.5f} seconds")
        try:
            print(termcolor.colored("************** End *************", "yellow"))
        except NameError:
            print("************** End *************")
    return wrapper


@speed_test_decorator
def sum_numbers(*numbers):
    print(f"Sum: {sum(numbers)}")


@speed_test_decorator
def counter_r(*numbers):
    if len(numbers) >= 2:
        for n in range(numbers[0], numbers[1] + 1):
            print(n)
    else:
        print("Put at least 2 numbers")


sum_numbers(2, 3, -5, 610, 23)
counter_r(1, 100)
print("")
print("------------------------------------")
print("")

# Lesson 086 - Zip Function
# Combines multiple iterables into tuples
print("Lesson 086 - Zip Function:")
names = ["ahmed", "mahmoud", "hamed", "nady"]
grades = [10, 20, 30]
print("Zip object:", zip(names, grades))
print("Zipped as list:", list(zip(names, grades)))

# Loop through zipped object
for name, grade in zip(names, grades):
    print(f"{name} => {grade}")

# Different length iterables
list1 = [1, 2, 3]
list2 = [10, 20]
list3 = [100, 200, 300, 400]
print("Zipped different lengths:", list(zip(list1, list2, list3)))
print("")
print("------------------------------------")
print("")

# Lesson 087 - Image Manipulation with Pillow
# Basic image operations using PIL
try:
    print("Lesson 087 - Image Manipulation:")
    # Replace with your image path
    my_image = Image.open(
        r"C:\Users\space\OneDrive\Pictures\GOB9PtOb0AAtaNL.jpg")
    my_image.show()

    # Crop image
    my_box = (0, 0, 400, 400)  # left, upper, right, lower
    my_cropped = my_image.crop(my_box)
    my_cropped.show()

    # Convert to grayscale
    my_grayscale = my_image.convert("L")
    my_grayscale.show()
except FileNotFoundError:
    print("Image file not found. Update the path to your image.")
except NameError:
    print("Pillow not installed. Run: pip install Pillow")
print("")
print("------------------------------------")
print("")

# Summary of Lessons 083 to 087
print("Summary:")
print("1 - Introduced decorators to wrap and enhance functions")
print("2 - Created advanced decorators with parameters and multiple layers")
print("3 - Built a practical decorator to measure execution time")
print("4 - Combined iterables using zip()")
print("5 - Manipulated images with Pillow (crop, grayscale)")
