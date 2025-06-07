# Mastering Python - Lessons 047 to 050
# Topic: While and For Loops in Python
# This code covers key concepts from Lessons 47 to 50 of the "Mastering Python" course by Elzero Web School:
# - Lesson 047: Introduction to while loops
# - Lesson 048: While loop training with lists
# - Lesson 049: Practical while loop application (website bookmarks)
# - Lesson 050: Introduction to for loops

# Lesson 047 - While Loop
# While loop runs as long as a condition is True
print("While loop examples:")
a = 11
while a < 10:
    print("hello")
    a += 1
# Example with break
while True:
    print("This will run once")
    break  # Exit the loop after one iteration
# Example with condition
condition = False
while condition:
    print("This will not run initially")
    condition = True  # If changed, loop would run next time
print("Done")
print("")
print("------------------------------------")
print("")

# Lesson 048 - While Loop Training
# Using while to iterate over a list
myf = ["mo", "ahmed", "khaled", "mahoud", "hedman", "saafaan", "ramdan", "nasser", "fady", "kholy"]
a = 0
print("Listing friends with while loop:")
while a < len(myf):
    print(f"#{str(a + 1).zfill(2)} {myf[a]}")  # zfill(2) pads number with zeros
    a += 1
else:
    print("LISTED FRIENDS ARE ON THE SCREEN")
print("")
print("------------------------------------")
print("")

# Lesson 049 - While Loop Practical
# Program to collect and display favorite websites
my_fav_web = []
bookedweb = 5
print("Website bookmark program:")
while bookedweb > 0:
    web = input(f"Enter your #{bookedweb} website? https:// ").lower().strip()
    my_fav_web.append(web)
    bookedweb -= 1
if len(my_fav_web) > 0:
    my_fav_web.sort()  # Sort websites alphabetically
    index = 0
    while index < len(my_fav_web):
        print(f"\nYour web number #{index + 1} is: https://{my_fav_web[index]}")
        index += 1
else:
    print("No websites added")
print("")
print("------------------------------------")
print("")

# Lesson 050 - For Loop
# For loop iterates over a sequence (list, string, etc.)
my_num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print("For loop examples:")
for number in my_num:
    if number % 2 == 0:
        print(f"{str(number).zfill(2)} is even")
    else:
        print(f"{str(number).zfill(2)} is odd")
else:
    print("Loop is finished")
# Loop over a string
name = "MOHAMED"
print("Looping over string:")
for letter in name:
    print(letter.lower())
print("")
print("------------------------------------")
print("")

# Summary of Lessons 047 to 050
print("Summary:")
print("1 - Used while loop to run code while a condition is True")
print("2 - Iterated over a list with while loop for training")
print("3 - Built a practical bookmark program with while loop")
print("4 - Used for loop to iterate over lists and strings")