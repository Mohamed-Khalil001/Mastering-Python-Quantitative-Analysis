# Mastering Python - Lessons 076 to 078
# Topic: Modules and Packages in Python
# This code covers key concepts from Lessons 76 to 78 of the "Mastering Python" course by Elzero Web School:
# - Lesson 076: Using built-in modules
# - Lesson 077: Creating and importing custom modules
# - Lesson 078: Installing and using external packages

# Lesson 076 - Built-in Modules
# Modules are files containing functions, classes, or variables
import random
import pkgutil
print("Lesson 076 - Built-in Modules:")
print("Random module path:", random)
print("Random float number:", random.random())
print("Random integer (0-20):", random.randint(0, 20))

# List all built-in modules
modules = [modname for _, modname, _ in pkgutil.iter_modules()]
print("Number of built-in modules:", len(modules))
print("Sample modules:", modules[:5])  # Show first 5 for brevity

# Inspect module functions
print("Functions in random module:", dir(random))
print("")
print("------------------------------------")
print("")

# Lesson 077 - Create Your Own Module
# Create a module file (e.g., quantmdu.py) and import it
# Example assumes quantmdu.py exists in the same directory with:
"""
# quantmdu.py
def summ(a, b):
    return a + b
def helloo(name):
    print(f"Hello {name}")
"""
try:
    import quantmdu
    print("Lesson 077 - Custom Module:")
    print("Functions in quantmdu:", dir(quantmdu))
    print("Sum from quantmdu:", quantmdu.summ(2, 4))
    quantmdu.helloo("Mohamed")

    # Import specific function
    from quantmdu import helloo as hh
    hh("Ahmed")

    # Import module with alias
    import quantmdu as qq
    print("Sum with alias:", qq.summ(10, 20))
except ModuleNotFoundError:
    print("Module quantmdu.py not found. Create it with the example code above.")
print("")
print("------------------------------------")
print("")

# Lesson 078 - External Packages
# Install packages using pip (e.g., termcolor, pyfiglet)
# Run in terminal: pip install termcolor pyfiglet
try:
    import termcolor
    import pyfiglet
    print("Lesson 078 - External Packages:")
    print("Functions in termcolor:", dir(termcolor)[:5])  # Show first 5
    print("Functions in pyfiglet:", dir(pyfiglet)[:5])  # Show first 5
    print(termcolor.colored("Mohamed", "yellow"))
    print(pyfiglet.figlet_format("Mohamed"))
    print(termcolor.colored(pyfiglet.figlet_format("Mohamed"), "yellow"))
except ModuleNotFoundError:
    print("Packages termcolor or pyfiglet not installed. Run: pip install termcolor pyfiglet")
print("")
print("------------------------------------")
print("")

# Summary of Lessons 076 to 078
print("Summary:")
print("1 - Used built-in modules like random and pkgutil")
print("2 - Created and imported a custom module (quantmdu)")
print("3 - Installed and used external packages (termcolor, pyfiglet)")
