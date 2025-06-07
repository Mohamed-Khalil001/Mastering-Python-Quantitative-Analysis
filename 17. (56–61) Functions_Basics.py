# Mastering Python - Lessons 056 to 061
# Topic: Functions Basics, Parameters, and Packing/Unpacking in Python
# This code covers key concepts from Lessons 56 to 61 of the "Mastering Python" course by Elzero Web School:
# - Lesson 056: Introduction to functions and return
# - Lesson 057: Function training with parameters
# - Lesson 058: Packing and unpacking parameters
# - Lesson 059: Default parameter values
# - Lesson 060: Packing/unpacking with dictionaries
# - Lesson 061: Mixed packing/unpacking with tuples and dictionaries

# Lesson 056 - Function and Return
# Functions are reusable blocks of code that can take parameters and return values
def first_function():
    print("Hello, that's my first function")
first_function()

def first_return_function():
    return "Hello, that's my first return function"
print(first_return_function())
print("")
print("------------------------------------")
print("")

# Lesson 057 - Functions Training
# Functions with parameters and type checking
a, b, c = 'mohamed', 'ahmed', 'nasser'
def hello_name(name):
    print(f"Hello {name}, thanks for subscribing!")
hello_name("kapaka")
hello_name(a)
hello_name(c)

def addition(n1, n2):
    if type(n1) != int or type(n2) != int:
        print("Please put two numbers")
    else:
        print(n1 + n2)
addition(100, 200)
addition(100, -200)
addition("jks", 100)

def full_name(first, middle, last):
    print(f"{first.strip().capitalize()} {middle.strip().capitalize():.1s} {last.strip().capitalize()}")
full_name("Mohamed", "Abdelfattah", "Khalil")
print("")
print("------------------------------------")
print("")

# Lesson 058 - Pack and Unpack for Functions
# Using * to unpack iterables or accept multiple arguments
lis = ["ahmed", "nasser", "mohamed", "khaled"]
print("List:", lis)
print("Unpacked list:", *lis)

def hello(*peoples):
    for name in peoples:
        print(f"Hello {name}")
hello(*lis)  # Unpack list as arguments
hello("zyad")  # Single argument
hello("ahmed", "nasser")  # Multiple arguments

def hello_with_country(country, *peoples):
    for name in peoples:
        print(f"Hello {name} from {country}")
hello_with_country("EGYPT", "ayad")
hello_with_country("EGYPT", "ahmed", "nasser")
print("")
print("------------------------------------")
print("")

# Lesson 059 - Default Value in Functions
# Parameters with default values
def person(name, age="unknown", country="unknown"):
    age_str = age if age == "unknown" else f"{int(age) * 12} months"
    print(f"Hello {name}, your age is {age_str} and your country is {country}")
person("Mohamed", "24", "Egypt")
person("Mohamed", "24")  # Uses default country
person("Mohamed")  # Uses default age and country
print("")
print("------------------------------------")
print("")

# Lesson 060 - Packing and Unpacking Arguments (Dictionary)
# Using ** to pack/unpack dictionaries
def show_skills(*skills):  # Tuple of skills
    print("Type of skills:", type(skills))
    for skill in skills:
        print(skill)
show_skills("python", "c++", "pbi")

def show_skills_dict(**skills):  # Dictionary of skills
    print("Type of skills:", type(skills))
    for skill, progress in skills.items():
        print(f"{skill:>11} => {progress}")
show_skills_dict(python=90, c=80, pbi=100)
myskills = {"py": 12, "sql": "10", "cpp": "20"}
show_skills_dict(**myskills)  # Unpack dictionary
print("")
print("------------------------------------")
print("")

# Lesson 061 - Mixed Packing and Unpacking
# Combining *args and **kwargs
my_skill_tuple = ("py", "c++", "sql")
my_skill_dict = {"py": 12, "sql": "30%", "cpp": "20%"}
def mskill(name, *myskillst, **myskillinprogress):
    print(f"Hello {name}\nYour skills without progress are:")
    for skill in myskillst:
        print(f"=> {skill}")
    print("Your skills with progress are:")
    for skill_key, skill_value in myskillinprogress.items():
        print(f"{skill_key} => {skill_value}")
mskill("mohamed", "python", "excel", py="20", cpp="100")
mskill("mohamed", *my_skill_tuple)  # Unpack tuple
mskill("mohamed", *my_skill_tuple, **my_skill_dict)  # Unpack tuple and dict
print("")
print("------------------------------------")
print("")

# Summary of Lessons 056 to 061
print("Summary:")
print("1 - Created and called functions with/without return values")
print("2 - Used parameters and type checking in functions")
print("3 - Handled multiple arguments with * unpacking")
print("4 - Set default values for function parameters")
print("5 - Packed/unpacked dictionaries with **")
print("6 - Combined *args and **kwargs for flexible functions")