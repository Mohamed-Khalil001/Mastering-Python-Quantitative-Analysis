# Mastering Python - Lessons 103 to 109
# Topic: Object-Oriented Programming (OOP) Basics
# This code covers key concepts from Lessons 103 to 109 of the "Mastering Python" course by Elzero Web School:
# - Lesson 103: Introduction to OOP concepts
# - Lesson 104: Class syntax and initialization
# - Lesson 105: Instance methods
# - Lesson 106: Class attributes
# - Lesson 107: Class and static methods
# - Lesson 108: Magic methods
# - Lesson 109: Inheritance

# Lesson 103 - Introduction to OOP
# OOP is about creating objects from classes (blueprints)
print("Lesson 103 - Introduction to OOP:")
name = "Mohamed"
print(f"Type of name: {type(name)}")
print(f"Class of name: {name.__class__}")
print("String methods:", dir(str)[:10], "...")  # Limited for brevity
print("Everything in Python is an object with a class!")
print("")
print("------------------------------------")
print("")

# Lesson 104 - Class Syntax and Info
# Classes define blueprints for objects with attributes and methods
print("Lesson 104 - Class Syntax and Info:")


class Dog:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        print(f"Dog {name} added")

    def __str__(self) -> str:
        return f"Dog: {self.name}, Age: {self.age}"

    def bark(self):
        print(f"{self.name} says hello!")


my_dog = Dog("Mimo", 4)
print(my_dog)
print(f"Name: {my_dog.name}")
print(f"Age: {my_dog.age}")
my_dog.bark()
print("")
print("------------------------------------")
print("")

# Lesson 105 - Instance Methods
# Instance methods take self to access instance attributes
print("Lesson 105 - Instance Methods:")


class Member:
    def __init__(self, fname: str, lname: str, gender: str = None):
        self.fname = fname
        self.lname = lname
        self.gender = gender

    def full_name(self) -> str:
        return f"Your full name is {self.fname} {self.lname}"

    def title_name(self) -> str:
        if self.gender == "Male":
            return f"Hello MR {self.fname} {self.full_name()}"
        elif self.gender == "Female":
            return f"Hello MISS {self.fname} {self.full_name()}"
        else:
            return f"Hello {self.fname} {self.full_name()}"


member1 = Member("Mohamed", "Abdelfattah", "Male")
member2 = Member("Yara", "Abdelfattah", "Female")
member3 = Member("Omar", "Abdelfattah")
print(member1.title_name())
print(member2.title_name())
print(member3.title_name())
print("")
print("------------------------------------")
print("")

# Lesson 106 - Class Attributes
# Class attributes are shared across all instances
print("Lesson 106 - Class Attributes:")


class Member:
    member_count = 0
    not_allowed_names = ["hell", "shit", "fuck"]

    def __init__(self, fname: str, lname: str, gender: str = None):
        if fname.lower() in self.not_allowed_names or lname.lower() in self.not_allowed_names:
            raise ValueError("Name is not valid")
        self.fname = fname
        self.lname = lname
        self.gender = gender
        Member.member_count += 1

    def full_name(self) -> str:
        return f"Your full name is {self.fname} {self.lname}"

    def title_name(self) -> str:
        if self.gender == "Male":
            return f"Hello MR {self.fname} {self.full_name()}"
        elif self.gender == "Female":
            return f"Hello MISS {self.fname} {self.full_name()}"
        else:
            return f"Hello {self.fname} {self.full_name()}"

    def delete_member(self) -> str:
        Member.member_count -= 1
        return f"User {self.fname} deleted"


print("Initial member count:", Member.member_count)
member1 = Member("Mohamed", "Abdelfattah", "Male")
member2 = Member("Yara", "Abdelfattah", "Female")
member3 = Member("Omar", "Abdelfattah")
print(member1.title_name())
print(member2.title_name())
print(member3.title_name())
print("Member count after adding:", Member.member_count)
print(member3.delete_member())
print("Member count after deletion:", Member.member_count)
# Uncomment to test invalid name
# member4 = Member("shit", "name", "Female")  # Raises ValueError
print("")
print("------------------------------------")
print("")

# Lesson 107 - Class Methods and Static Methods
# Class methods operate on the class; static methods are utility functions
print("Lesson 107 - Class and Static Methods:")


class Member:
    member_count = 0
    not_allowed_names = ["hell", "shit", "fuck"]
    members_names = []

    @classmethod
    def member_names_list(cls) -> list:
        return cls.members_names

    @staticmethod
    def hello_member() -> str:
        return "Hello from static method"

    def __init__(self, fname: str, lname: str, gender: str = None):
        if fname.lower() in self.not_allowed_names or lname.lower() in self.not_allowed_names:
            raise ValueError("Name is not valid")
        self.fname = fname
        self.lname = lname
        self.gender = gender
        Member.members_names.append(f"{fname} {lname}")
        Member.member_count += 1

    def full_name(self) -> str:
        return f"Your full name is {self.fname} {self.lname}"

    def title_name(self) -> str:
        if self.gender == "Male":
            return f"Hello MR {self.fname} {self.full_name()}"
        elif self.gender == "Female":
            return f"Hello MISS {self.fname} {self.full_name()}"
        else:
            return f"Hello {self.fname} {self.full_name()}"


member1 = Member("Mohamed", "Abdelfattah", "Male")
member2 = Member("Yara", "Abdelfattah", "Female")
print("Member names (class method):", Member.member_names_list())
print("Static method:", Member.hello_member())
print("Static method via instance:", member1.hello_member())
print("")
print("------------------------------------")
print("")

# Lesson 108 - Magic Methods
# Magic methods customize object behavior
print("Lesson 108 - Magic Methods:")


class Person:
    def __init__(self, name: str = "unknown", members: list = None):
        self.name = name
        self.members = members if members is not None else []

    def hello(self) -> str:
        return f"Hello {self.name}"

    def __str__(self) -> str:
        return self.hello()

    def members_list(self):
        for member in self.members:
            print(member)

    def __len__(self) -> int:
        return len(self.members)


group = Person("Leader", ["Mohamed", "Ahmed", "Omar"])
print("String representation:", group)  # Uses __str__
group.members_list()
print("Length of members:", len(group))  # Uses __len__
print("")
print("------------------------------------")
print("")

# Lesson 109 - Inheritance
# Classes can inherit attributes and methods from other classes
print("Lesson 109 - Inheritance:")


class Fruit:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price
        print("Hello from main class")

    def hello(self, name: str):
        print(f"Hello from main class, fruit name is {self.name}")


class Orange(Fruit):
    def __init__(self, name: str, price: int):
        super().__init__(name, price)
        print("Hello from derived class")

    def color(self):
        print("Red color")


fruit1 = Orange("Orange", 44)
fruit1.hello("Jidkl")
fruit1.color()
print("")
print("------------------------------------")
print("")

# Summary of Lessons 103 to 109
print("Summary:")
print("1 - Introduced OOP concepts (classes as blueprints, objects as instances)")
print("2 - Defined classes with __init__ and instance attributes")
print("3 - Created instance methods to operate on object data")
print("4 - Used class attributes shared across instances")
print("5 - Implemented class and static methods for class-level operations")
print("6 - Customized objects with magic methods like __str__ and __len__")
print("7 - Demonstrated inheritance to reuse and extend class functionality")
