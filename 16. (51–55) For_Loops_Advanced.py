# Mastering Python - Lessons 051 to 055
# Topic: Advanced For Loops and Control in Python
# This code covers key concepts from Lessons 51 to 55 of the "Mastering Python" course by Elzero Web School:
# - Lesson 051: For loop training with range
# - Lesson 052: Looping over dictionaries
# - Lesson 053: Nested for loops for complex iterations
# - Lesson 054: Using break, continue, and pass for loop control
# - Lesson 055: Advanced dictionary looping with items()

# Lesson 051 - For Loop Training
# Using range() for controlled iterations
print("For loop with range examples:")
grades = range(0, 101)
for grade in grades:
    print(grade)
print("Print every second number from 0 to 10:")
for num in range(0, 11, 2):  # Start, end, step
    print(num)
print("")
print("------------------------------------")
print("")

# Lesson 052 - Loop On Dictionary
# Loop over dictionary keys and access values
my_skills = {
    "python": "5%",
    "power bi": "20%",
    "sql": "1%",
    "pexcel": "7%",
    "c++": "3%",
    "power query": "10%"
}
print("Looping over dictionary keys:")
for skill in my_skills:
    print(f"My progress in {skill:<11} skill = {my_skills[skill]}")
print("")
print("------------------------------------")
print("")

# Lesson 053 - Nested For Loop
# Nested loops to iterate over multiple levels
my_team = {
    "mohamed": {
        "python": "5%",
        "power bi": "20%",
        "sql": "1%",
        "pexcel": "7%",
        "c++": "3%",
        "power query": "10%"
    },
    "ahmed": {
        "python": "20%",
        "power bi": "30%",
        "sql": "14%",
        "pexcel": "75%",
        "c++": "3%",
        "power query": "15%"
    },
    "khaled": {
        "python": "55%",
        "power bi": "25%",
        "sql": "16%",
        "pexcel": "78%",
        "c++": "39%",
        "power query": "99%"
    }
}
print("Nested for loop example:")
for member in my_team:
    print(f"\n########### {member} ##############")
    for skill in my_team[member]:
        print(f"{skill:>11} => {my_team[member][skill]}")
print("")
print("------------------------------------")
print("")

# Lesson 054 - Break, Continue, Pass
# Control flow in loops
m_nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Using continue (skip 6):")
for num in m_nums:
    if num == 6:
        continue  # Skip 6, continue to next iteration
    print(num)
print("*" * 50)
print("Using break (stop at 6):")
for num in m_nums:
    if num == 6:
        break  # Stop loop at 6
    print(num)
print("*" * 50)
print("Using pass (placeholder):")
for num in m_nums:
    if num == 6:
        pass  # Placeholder, no action, avoids error
    print(num)
print("")
print("------------------------------------")
print("")

# Lesson 055 - Advanced Dictionary Loop
# Loop over dictionary using items() for keys and values
print("Advanced dictionary loop with items():")
for member, skills in my_team.items():
    print(f"########### {member} ##########")
    for skill, progress in skills.items():
        print(f"{skill:>11} => {progress}")
print("")
print("------------------------------------")
print("")

# Summary of Lessons 051 to 055
print("Summary:")
print("1 - Used range() for controlled for loop iterations")
print("2 - Looped over dictionary keys to access values")
print("3 - Used nested for loops for multi-level data")
print("4 - Controlled loops with break, continue, and pass")
print("5 - Advanced looping over dictionaries with items()")