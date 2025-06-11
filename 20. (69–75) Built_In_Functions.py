# Mastering Python - Lessons 069 to 075
# Topic: Built-in Functions in Python
# This code covers key concepts from Lessons 69 to 75 of the "Mastering Python" course by Elzero Web School:
# - Lesson 069: Brief review of all(), any(), bin(), id()
# - Lesson 070: sum(), round(), range(), print()
# - Lesson 071: abs(), pow(), min(), max(), slice()
# - Lesson 072: map()
# - Lesson 073: filter()
# - Lesson 074: reduce()
# - Lesson 075: enumerate(), help(), reversed()

from functools import reduce

# Lesson 069 - Built-in Functions (Review)
# Quick recap of all, any, bin, id
print("Lesson 069 - Review of all, any, bin, id:")
x = [1, 2, 3, 5, 6, ()]
print("all([1, 2, 3, 5, 6, ()]):", all(x))  # False due to empty tuple
print("any([1, 2, 3, 5, 6, ()]):", any(x))  # True due to numbers
print("bin(10):", bin(10))  # 0b1010
a, b = 2, 5
print("id(2):", id(a), "id(5):", id(b))
print("")
print("------------------------------------")
print("")

# Lesson 070 - Built-in Functions (sum, round, range, print)
print("Lesson 070 - sum, round, range, print:")
# sum(iterable, start)
gigs = [12.05, 5.4, 4.40, 2.6]
print("sum(gigs):", sum(gigs))
print("sum(gigs, 40):", sum(gigs, 40))

# round(number, digits)
n, m = 66.7568, 66.4568
print("round(66.7568):", round(n))
print("round(66.4568, 2):", round(m, 2))

# range(start, end, step)
print("list(range(10)):", list(range(10)))
print("list(range(0, 20, 2)):", list(range(0, 20, 2)))

# print() with sep and end
print("hello", "world", "in", "war", "wide", sep="|")
print("the end", end=" @ ")
print("is here")
print("")
print("------------------------------------")
print("")

# Lesson 071 - Built-in Functions (abs, pow, min, max, slice)
print("Lesson 071 - abs, pow, min, max, slice:")
# abs()
aa = [-100, 200, 10, -1, -20.6]
print("abs(-20.6):", abs(-20.6))

# pow(base, exp, mod)
print("pow(2, 5):", pow(2, 5))
print("pow(2, 5, 2):", pow(2, 5, 2))

# min() and max()
print("min(aa):", min(aa))
print("max(aa):", max(aa))
print("min('mohamed', 'zeyad', 'amr'):", min("mohamed", "zeyad", "amr"))

# slice(start, end, step)
my_list = ["apple", "banana", "cherry", "date", "elderberry"]
s = slice(1, 4)
print("slice(1, 4) on my_list:", my_list[s])
print("")
print("------------------------------------")
print("")

# Lesson 072 - Built-in Function (map)
# Apply function to each element in iterable
print("Lesson 072 - map:")
num = [1, 2, 3, 4, 5]


def plus_10(x):
    return x + 10


print("map with def function:", list(map(plus_10, num)))
print("map with lambda:", list(map(lambda x: x + 10, num)))
print("map with built-in (str):", tuple(map(str, num)))

# Map object is lazy and single-use
y = map(plus_10, num)
print("Map object:", y)
print("First use:", list(y))
print("Second use:", list(y))  # Empty because map is exhausted
print("")
print("------------------------------------")
print("")

# Lesson 073 - Built-in Function (filter)
# Filter elements based on a boolean function
print("Lesson 073 - filter:")
nums = [0, 2, 0, 12, 10, 20, 0, 2, 33]


def check_number(num):
    return num > 10


print("filter > 10:", list(filter(check_number, nums)))


def check_zero(num):
    return num == 0


print("filter zeros:", list(filter(check_zero, nums)))

print("filter with lambda > 10:", list(filter(lambda num: num > 10, nums)))

# Example with strings


def oname(name):
    return str(name).startswith("o")


myfriends = ("ahmed", "osama", "omar", "omer")
print("filter names starting with 'o':", list(filter(oname, myfriends)))
print("")
print("------------------------------------")
print("")

# Lesson 074 - Built-in Function (reduce)
# Reduce iterable to a single value
print("Lesson 074 - reduce:")
numbers = [1, 8, 2, 9, 100]


def sum_all(num1, num2):
    return num1 + num2


print("reduce sum:", reduce(sum_all, numbers))
print("reduce multiply with lambda:", reduce(lambda x, y: x * y, numbers))


def max_num(x, y):
    return x if x > y else y


print("reduce max:", reduce(max_num, numbers))
print("")
print("------------------------------------")
print("")

# Lesson 075 - Built-in Functions (enumerate, help, reversed)
print("Lesson 075 - enumerate, help, reversed:")
# enumerate(iterable, start)
skills = ["python", "c++", "sql", "power bi", "tableau", "data analysis"]
for counter, skill in enumerate(skills, 1):
    print(f"{counter} => {skill}")

# help()
# print(help(print))  # Uncomment to see help for print

# reversed()
nam = "mohamed"
print("reversed 'mohamed':", list(reversed(nam)))
skillsy = list(enumerate(skills))
print("Reversed enumerate:", [(c, s) for c, s in reversed(skillsy)])
print("")
print("------------------------------------")
print("")

# Summary of Lessons 069 to 075
print("Summary:")
print("1 - Reviewed all(), any(), bin(), id()")
print("2 - Used sum(), round(), range(), and print() with custom separators")
print("3 - Applied abs(), pow(), min(), max(), and slice()")
print("4 - Mapped functions over iterables with map()")
print("5 - Filtered elements with filter() based on conditions")
print("6 - Reduced iterables to single values with reduce()")
print("7 - Enumerated, accessed help, and reversed iterables")
