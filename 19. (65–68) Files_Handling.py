# Mastering Python - Lessons 065 to 069
# Topic: File Handling and Built-in Functions in Python
# This code covers key concepts from Lessons 65 to 69 of the "Mastering Python" course by Elzero Web School:
# - Lesson 065: File handling basics (opening, modes)
# - Lesson 066: Reading files (read, readline, readlines)
# - Lesson 067: Writing and appending to files
# - Lesson 068: Truncate, tell, seek, and file removal
# - Lesson 069: Built-in functions (all, any, bin, id)

import os

# Lesson 065 - File Handling Basics
# File modes: r (read), w (write), a (append), x (create)
print("File handling basics:")
print("Current working directory:", os.getcwd())
print("This script's absolute path:", os.path.abspath(__file__))
print("This script's directory:", os.path.dirname(os.path.abspath(__file__)))

# Change directory (example, adjust path as needed)
# os.chdir(r"C:\Users\space\Downloads\Q_A\projects\projects(stage1_python)")
# print("New working directory:", os.getcwd())

# Open a file (assumes firstpyfile.txt exists in current directory)
try:
    fileee = open("firstpyfile.txt", "r")
    print("Text file path:", os.path.abspath("firstpyfile.txt"))
    fileee.close()
except FileNotFoundError:
    print("File not found, please create firstpyfile.txt")
print("")
print("------------------------------------")
print("")

# Lesson 066 - Read Files
# Methods to read file content
print("Reading file examples:")
try:
    myfile = open("firstpyfile.txt", "r")
    print("File name:", myfile.name)
    print("File mode:", myfile.mode)
    print("File encoding:", myfile.encoding)

    # read() - read entire file
    myfile.seek(0)  # Reset cursor to start
    print("Entire content:", myfile.read())

    # readline() - read one line
    myfile.seek(0)
    print("First line:", myfile.readline().strip())
    print("Second line:", myfile.readline().strip())

    # readlines() - read all lines as list
    myfile.seek(0)
    print("All lines as list:", myfile.readlines())

    # Read specific bytes
    myfile.seek(0)
    print("First 32 bytes:", myfile.readlines(32))

    # Loop through lines
    myfile.seek(0)
    for line in myfile:
        print("Line:", line.strip())
        if line.startswith("11"):
            break
    myfile.close()
except FileNotFoundError:
    print("File not found for reading")
print("")
print("------------------------------------")
print("")

# Lesson 067 - Write and Append in Files
# Writing and appending to files
print("Writing and appending examples:")
myfile = open("myfile.txt", "w")  # Create/overwrite file
myfile.write("Hello, this is my first file\n")
myfile.write("Hello, I am Mohamed\n")
myfile.write("Nice to write you\n")
mylist = ["Mohamed\n", "Omar\n", "Amar\n", "Hemdan\n"]
myfile.writelines(mylist)
myfile.close()

# Append to existing file
myfile = open("myfile.txt", "a")
myfile.write("Appended line\n")
myfile.close()

# Read to verify
myfile = open("myfile.txt", "r")
print("File content after write/append:", myfile.read())
myfile.close()
print("")
print("------------------------------------")
print("")

# Lesson 068 - Truncate, Tell, Seek, and File Removal
# Advanced file operations
print("Advanced file operations:")
myfile = open("myfile.txt", "a")
myfile.truncate(50)  # Truncate to 50 bytes
myfile.close()

myfile = open("myfile.txt", "r")
print("File after truncate:", myfile.read())
myfile.seek(0)
print("Current cursor position:", myfile.tell())  # Get cursor position
myfile.seek(10)  # Move cursor to byte 10
print("Content from byte 10:", myfile.read())
myfile.close()

# Remove file (uncomment to test)
# os.remove("myfile.txt")
# print("File removed")
print("")
print("------------------------------------")
print("")

# Lesson 069 - Built-in Functions (all, any, bin, id)
# Useful built-in functions
print("Built-in functions examples:")
# all() - True if all elements are truthy
x = [1, 2, 3, 5, 6, ()]
print("all([1, 2, 3, 5, 6, ()]):", all(x))  # False due to empty tuple
x = [1, 2, 3, 5, 6]
print("all([1, 2, 3, 5, 6]):", all(x))  # True

# any() - True if at least one element is truthy
x = [1, 2, 3, 5, 6, ()]
print("any([1, 2, 3, 5, 6, ()]):", any(x))  # True due to numbers
x = [[], 0, ()]
print("any([[], 0, ()]):", any(x))  # False

# bin() - Convert to binary
print("bin(10):", bin(10))  # 0b1010
print("bin(12):", bin(12))  # 0b1100

# id() - Get memory address
a = 2
b = 5
print("id(2):", id(a))
print("id(5):", id(b))
print("")
print("------------------------------------")
print("")

# Summary of Lessons 065 to 069
print("Summary:")
print("1 - Learned file handling basics: opening, modes, and paths")
print("2 - Read files using read(), readline(), readlines(), and loops")
print("3 - Wrote and appended to files with write() and writelines()")
print("4 - Used truncate(), tell(), seek(), and os.remove() for file control")
print("5 - Explored built-in functions: all(), any(), bin(), id()")
