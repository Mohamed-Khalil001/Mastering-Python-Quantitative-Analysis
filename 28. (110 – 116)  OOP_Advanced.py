# Mastering Python - Lessons 110 to 116
# Topic: Advanced Object-Oriented Programming (OOP) in Python
# This code covers key concepts from Lessons 110 to 116 of the "Mastering Python" course by Elzero Web School:
# - Lesson 110: Multiple inheritance
# - Lesson 111: Polymorphism
# - Lesson 112: Encapsulation (public, protected, private)
# - Lesson 113: Getter and setter methods
# - Lesson 114: @property decorator
# - Lesson 115: Abstract base classes (ABCs)
# - Lesson 116: SQLite database introduction (commented out for reference)

from abc import ABC, abstractmethod

# Lesson 110 - Multiple Inheritance
# A class can inherit from multiple parent classes
print("Lesson 110 - Multiple Inheritance:")


class BaseOne:
    def __init__(self):
        print("From BaseOne")


class BaseTwo:
    def __init__(self):
        print("From BaseTwo")


class Derived(BaseOne, BaseTwo):
    def __init__(self):
        super().__init__()  # Calls BaseOne.__init__ (MRO order)
        print("From Derived")


print("Method Resolution Order (MRO):", Derived.mro())
my_instance = Derived()
print("\nExample with Fruit:")


class Fruit:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price
        print("Hello from Fruit class")

    def hello(self, name: str):
        print(f"Hello from Fruit, fruit name is {self.name}")


class Orange(Fruit):
    def __init__(self, name: str, price: int):
        super().__init__(name, price)
        print("Hello from Orange class")

    def color(self):
        print("Red color")


fruit1 = Orange("Orange", 44)
fruit1.hello("Jidkl")
fruit1.color()
print("")
print("------------------------------------")
print("")

# Lesson 111 - Polymorphism
# Same method behaves differently in different classes
print("Lesson 111 - Polymorphism:")
# Example with built-in types
n1, n2 = 10, 20
s1, s2 = "Mohamed", "Abdelfattah"
print(f"Polymorphism with +: {n1 + n2} (int) vs {s1 + s2} (str)")
print(
    f"Polymorphism with len: {len([1, 2, 3])}, {len(('a', 'b'))}, {len({'k': 1})}")

# Example with classes


class One:
    def describe(self):
        print("From class One")
        # raise NotImplementedError("Derived class must implement this method")


class Derived1(One):
    def describe(self):
        print("From class Derived1")


class Derived2(One):
    pass


polym1 = Derived1()
polym1.describe()
# polym2 = Derived2()  # Would raise NotImplementedError if uncommented
# polym2.describe()
print("")
print("------------------------------------")
print("")

# Lesson 112 - Encapsulation
# Restricting access to attributes and methods
print("Lesson 112 - Encapsulation:")


class Member:
    def __init__(self, name: str):
        self.name = name  # Public
        self._protected_name = name  # Protected
        self.__private_name = name  # Private

    def display(self):
        print(f"Public: {self.name}")
        print(f"Protected: {self._protected_name}")
        print(f"Private: {self.__private_name}")


member = Member("Ahmed")
print("Accessing public:", member.name)
print("Accessing protected:", member._protected_name)
# print(member.__private_name)  # AttributeError
member.display()
print("")
print("------------------------------------")
print("")

# Lesson 113 - Getter and Setter Methods
# Control access to private attributes
print("Lesson 113 - Getter and Setter Methods:")


class Member:
    def __init__(self, name: str):
        self.__name = name

    def say_hello(self) -> str:
        return f"Hello {self.__name}"

    def get_name(self) -> str:
        return self.__name

    def set_name(self, new_name: str):
        self.__name = new_name


member = Member("Mohamed")
print("Get name:", member.get_name())
member.set_name("Ahmed")
print("After set name:", member.get_name())
print(member.say_hello())
print("")
print("------------------------------------")
print("")

# Lesson 114 - @property Decorator
# Simplify getter/setter with properties
print("Lesson 114 - @property Decorator:")


class Member:
    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age

    def say_hello(self) -> str:
        return f"Hello {self.__name}"

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, new_name: str):
        self.__name = new_name

    @property
    def age_in_days(self) -> int:
        return self.__age * 365


member = Member("Mohamed", 24)
print("Name:", member.name)
print("Age in days:", member.age_in_days)
member.name = "Ahmed"
print("Updated name:", member.name)
# print(member.age_in_days())  # Error: age_in_days is a property, not a method
print("")
print("------------------------------------")
print("")

# Lesson 115 - Abstract Base Classes (ABCs)
# OOP => ABCs => Abstract base class
# ----------------
# class called abstract class if it has one oe more abstract methods
# abc module in python provides infrastructure for  defining custom abstract base classes
# by adding @abstractmethod decorator on the merhods
# ABCMeta -Class is a metaclass used for defining abstract base class

# Enforce method implementation in derived classes
print("Lesson 115 - Abstract Base Classes:")


class Programming(ABC):
    @abstractmethod
    def has_oop(self) -> str:
        pass


class Python(Programming):
    def has_oop(self) -> str:
        return "Yes"


class Pascal(Programming):
    def has_oop(self) -> str:
        return "No"


class Cpp(Programming):
    def has_oop(self) -> str:
        return "Yes"


py = Python()
pas = Pascal()
cpp = Cpp()
print("Python has OOP:", py.has_oop())
print("Pascal has OOP:", pas.has_oop())
print("C++ has OOP:", cpp.has_oop())
print("")
print("------------------------------------")
print("")

# Lesson 116 - SQLite Database Introduction
# # # --Databases => Into --
# # # ----------------------------------------------
# # # Database is the place where we can store data
# # # Data organised into tables (users , categories )
# # # tables has columns (id , username , password )
# # # there's many types of databases (mongodb , mysql , sqllite)
# # # sql stand for structured query language
# # # sqlite => can run in memory or in a single file
# # # you can browse file with http://sqlitebrowser.org/
# # # gata inside database has types (text , integer , date )
# Commented out as it aligns with Lesson 117 in the course

print("Lesson 116 - SQLite Database Introduction (Reference):")
"""
# SQLite is a lightweight database that stores data in a single file
# Use sqlite3 module to interact with SQLite databases
# Tables organize data with columns (e.g., id, username)
# SQL is used to query databases
# Browse SQLite files with http://sqlitebrowser.org/
# Example (uncomment to run):
import sqlite3
db = sqlite3.connect("app.db")
db.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER, name TEXT)")
db.close()
"""
print("SQLite content moved to Lessons 117+ for database operations")
print("")
print("------------------------------------")
print("")

# Summary of Lessons 110 to 116
print("Summary:")
print("1 - Demonstrated multiple inheritance and MRO")
print("2 - Implemented polymorphism with methods and built-in operators")
print("3 - Applied encapsulation with public, protected, and private attributes")
print("4 - Controlled access with getter and setter methods")
print("5 - Simplified access with @property decorator")
print("6 - Enforced method implementation with abstract base classes")
print("7 - Introduced SQLite databases (details in Lessons 117+)")
