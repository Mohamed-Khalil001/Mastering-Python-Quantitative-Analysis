# Mastering Python - Lessons 041 to 046
# Topic: Control Flow, Conditions, and Membership in Python
# This code covers key concepts from Lessons 41 to 46 of the "Mastering Python" course by Elzero Web School:
# - Lesson 041: Using if, elif, and else for decisions
# - Lesson 042: Nested if statements for complex conditions
# - Lesson 043: Short if (ternary) conditions
# - Lesson 044: Practical if training with user choice
# - Lesson 045: Membership operators (in, not in)
# - Lesson 046: Practical membership control example

# Lesson 041 - If, Elif, Else
# Basic conditional statements for decision-making
name = input("What's your name? ").strip().capitalize()
print("Select your country:")
print("\t1- EGYPT\n\t2- KSA\n\t3- KWUIT\n\t4- SOUDAIN\n\t5- SURIA\n\t6- LIBNAN\n\t7- PALSTIN\n\t8- ORDON\n\t9- EMIRATES\n\t10- SOMAL\n\t11- IRAQ\n\t12- Others")
country = input("What's your country? ").strip().upper()
cname = "Financial Quantitative Analysis"
clength = "120 credit hour"
cprice = 100
if country in ["EGYPT", "PALSTIN", "SURIA", "SOUDAIN"]:
    print(f"\n\tHello {name}, {cname} course with {clength} is available for {country} by {cprice - (cprice * 80 / 100)}\n")
elif country in ["LIBNAN", "ORDON", "SOMAL", "IRAQ"]:
    print(f"\n\tHello {name}, {cname} course with {clength} is available for {country} by {cprice - (cprice * 60 / 100)}\n")
elif country in ["KWUIT", "EMIRATES", "KSA"]:
    print(f"\n\tHello {name}, {cname} course with {clength} is available for {country} by {cprice - (cprice * 3 / 100)}\n")
elif country == "OTHERS":
    print(f"\n\tHello {name}, {cname} course with {clength} is available for you by {cprice - (cprice * 30 / 100)}\n")
else:
    print("Please write the correct country 😤")
print("")
print("------------------------------------")
print("")

# Lesson 042 - Nested If
# Nested conditions for more complex decisions
cname = "Data Analysis by Python"
ucountry = "PALSTIN"
student = "Yes"
cprice = 100
level = 2
print("Nested if example:")
if ucountry == "EGYPT" or ucountry == "PALSTIN":
    if student == "Yes":
        if level >= 4:
            print(f"AS YOU FROM {ucountry} and STUDENT with level {level}, {cname} course is {cprice - 50}$ for you")
        else:
            print(f"AS YOU FROM {ucountry} and STUDENT with level {level}, {cname} course is {cprice - 40}$ for you")
    else:
        print(f"AS YOU FROM {ucountry}, {cname} course is {cprice - 20}$ for you")
print("")
print("------------------------------------")
print("")

# Lesson 043 - Short If Condition
# Ternary operator for concise if-else statements
movage = 18
age = 16
print("Short if example:")
if age < movage:
    print("Movie is not good for you 😴")
else:
    print("Movie is good for you 🥰")
print("Movie is good for you" if age > 18 else "Movie is not good for you")
print("")
print("------------------------------------")
print("")

# Lesson 044 - Practical If Training
# Program to calculate age in user-chosen unit
print("&" * 100)
print("You can write full name of the unit or only the first letter".capitalize().center(100, "&"))
print("&" * 100)
years = int(input("\nWhat's your age?! ").strip())
months = years * 12
weeks = months * 4
days = weeks * 7
hours = days * 24
unit = input("What unit do you want? Month, Week, Day, or Hour\n").lower().strip()
if unit in ["month", "months", "m"]:
    print(f"\n\tYour age by {unit} is {months:,} month 🥰\n")
elif unit in ["week", "weeks", "w"]:  # Fixed: changed 'or' to 'in' for correct logic
    print(f"\n\tYour age by {unit} is {weeks:,} week 😄\n")
elif unit in ["day", "days", "d"]:
    print(f"\n\tYour age by {unit} is {days:,} day 😂\n")
elif unit in ["hour", "hours", "h"]:
    print(f"\n\tYour age by hours is {hours:,} hours 🤣\n")
else:
    print("Please write the correct unit!! 😴😪")
print("")
print("------------------------------------")
print("")

# Lesson 045 - Membership Operators
# 'in' and 'not in' to check membership in strings, lists, etc.
print("Membership operators example:")
# String
name = "Mohamed Abdelfattah Mohamed"
print("Abdelfattah in name:", "Abdelfattah" in name)
print("mo in name:", "mo" in name)
print("Mo in name:", "Mo" in name)
# List
friend_names = ["Ahmed", "Nasser", "Kholy", "Bakry"]
print("Nasser in friend_names:", "Nasser" in friend_names)
# Using in and not in with conditions
countries_1 = ["EGYPT", "PALSTIN", "SURIA"]
countries_2 = ["SUDIA", "EMIRATES", "KWUIT"]
discount_1 = 80
discount_2 = 10
country = "SUDIA"
if country in countries_1:
    print(f"Your discount is {discount_1}%")
elif country in countries_2:
    print(f"Your discount is {discount_2}%")
elif country not in countries_1 + countries_2:  # Fixed: corrected typo in 'countries_2'
    print("Your discount is 5%")
print("")
print("------------------------------------")
print("")

# Lesson 046 - Membership Control Practical
# Admin project: manage a list with membership checks
admins = ["mohamed", "ahmed", "osama", "amr"]
name = input("Enter your name?! ").strip().lower()
if name in admins:
    print("You are an admin")
    option = input("Do you want Update or Delete?! ").lower().strip()
    if option == "update":
        newname = input("Put the new name? ").strip().lower()
        admins[admins.index(name)] = newname
        print("Your update is done")
        print(admins)
    elif option == "delete":
        admins.remove(name)
        print("You deleted from admins")
        print(admins)
else:
    print("You are not admin")
    adding = input("Do you want to add your name? Y or N ").strip().lower()
    if adding == "y":
        newadmin = input("What name do you want to add?! ").strip().lower()
        admins.append(newadmin)
        print("You added to admin list")
        print(admins)
    else:
        print("You are not admin so you cannot access")
print("")
print("------------------------------------")
print("")

# Summary of Lessons 041 to 046
print("Summary:")
print("1 - Used if, elif, else for basic decisions")
print("2 - Applied nested if for complex conditions")
print("3 - Used short if (ternary) for concise checks")
print("4 - Built practical age calculator with user-chosen unit")
print("5 - Checked membership with 'in' and 'not in' operators")
print("6 - Created admin project with membership control")