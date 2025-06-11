# Mastering Python - Lessons 095 to 102
# Topic: Regular Expressions in Python
# This code covers key concepts from Lessons 95 to 102 of the "Mastering Python" course by Elzero Web School:
# - Lesson 095: Introduction to regular expressions
# - Lesson 096: Quantifiers in regular expressions
# - Lesson 097: Character classes in regular expressions
# - Lesson 098: Logical OR and escaping in regular expressions
# - Lesson 099: Grouping in regular expressions
# - Lesson 100: Using re.search and re.findall
# - Lesson 101: Using re.split and re.sub
# - Lesson 102: Group trainings and flags in regular expressions

import re

# Lesson 095 - Regular Expression Introduction
# Regex defines search patterns for text processing
print("Lesson 095 - Regular Expression Introduction:")
text = "Visit our site at www.example.com or contact us at support@example.org"
# Simple pattern to find a word
pattern = r"example"
matches = re.findall(pattern, text)
print(f"Found '{pattern}': {matches}")
print("Resources: Test regex at https://pythex.org")
print("Regex cheatsheet: https://www.debuggex.com/cheatsheet/regex/python")
print("")
print("------------------------------------")
print("")

# Lesson 096 - Regular Expression Quantifiers
# Quantifiers specify how many times a pattern should match
print("Lesson 096 - Regular Expression Quantifiers:")
# Quantifiers: * (0+), + (1+), ? (0 or 1), {n} (exactly n), {n,m} (n to m), {n,} (n+)
text = "a ab aa abb aaaa"
print(f"Text: {text}")
print("* (0 or more):", re.findall(r"ab*", text))  # a, ab, abb
print("+ (1 or more):", re.findall(r"ab+", text))  # ab, abb
print("? (0 or 1):", re.findall(r"ab?", text))  # a, ab, ab
print("{2} (exactly 2):", re.findall(r"ab{2}", text))  # abb
print("{2,4} (2 to 4):", re.findall(r"ab{2,4}", text))  # abb, aaaa
print("{2,} (2 or more):", re.findall(r"ab{2,}", text))  # abb, aaaa
print("")
print("------------------------------------")
print("")

# Lesson 097 - Regular Expression Character Classes
# Character classes match specific sets of characters
print("Lesson 097 - Character Classes:")
text = "123 abc ABC !@#  \t\n"
print(f"Text: {text}")
print("[a-c]:", re.findall(r"[a-c]", text))  # a, b, c
print("[^a-c] (not a-c):", re.findall(r"[^a-c]", text))  # 1,2,3, A,B,C, !,@,#, \t,\n
print(r"\d (digit):", re.findall(r"\d", text))  # 1, 2, 3
print(r"\D (non-digit):", re.findall(r"\D", text))  # a,b,c, A,B,C, !,@,#, \t,\n
print(r"\s (whitespace):", re.findall(r"\s", text))  # \t, \n
print(r"\S (non-whitespace):", re.findall(r"\S", text))  # 1,2,3, a,b,c, A,B,C, !,@,#
print(r"\w (word char):", re.findall(r"\w", text))  # 1,2,3, a,b,c, A,B,C
print(r"\W (non-word char):", re.findall(r"\W", text))  # !,@,#, \t,\n
print("")
print("------------------------------------")
print("")

# Lesson 098 - Logical OR and Escaping
# Using | for OR and \ for escaping special characters
print("Lesson 098 - Logical OR and Escaping:")
texts = ["hello world", "world hello", "color", "colour", "https://example.com"]
print("Text list:", texts)
print("^hello (starts with hello):")
for text in texts:
    if re.match(r"^hello", text):
        print(f"✅ {text}")
print("\ncolou?r (color or colour):")
for text in texts:
    if re.search(r"colou?r", text):
        print(f"✅ {text}")
print("")
print("------------------------------------")
print("")

# Lesson 099 - Grouping
# Using () to group patterns
print("Lesson 099 - Grouping:")
# Example 1: List items like "1-HTML", "2)CSS", "3>PHP"
text = "1-HTML 2)CSS 3>PHP"
pattern = r"(\d[-)>])\s?(\w+)"
matches = re.findall(pattern, text)
print(f"List items pattern: {pattern}")
print("Matches:", matches)  # [('1-', 'HTML'), ('2)', 'CSS'), ('3>', 'PHP')]

# Example 2: Phone numbers like "012 4578 213", "011 4568 (345)"
text = "012 4578 213 011 4568 (345)"
pattern = r"\d{3}\s\d{4}\s(\d{3}|\(\d{3}\))"
matches = re.findall(pattern, text)
print(f"Phone number pattern: {pattern}")
print("Matches:", matches)  # ['213', '(345)']

# Example 3: URLs like "http://www.elzero.net", "https://elzero.org"
text = "http://www.elzero.net https://elzero.org http://elzero.com"
pattern = r"https?://(www\.)?(\w+\.)(net|org|com)"
matches = re.findall(pattern, text)
print(f"URL pattern: {pattern}")
print("Matches:", matches)  # [('www.', 'elzero.', 'net'), ('', 'elzero.', 'org'), ('', 'elzero.', 'com')]
print("")
print("------------------------------------")
print("")

# Lesson 100 - Re Module Search and Findall
# search() returns first match; findall() returns all matches
print("Lesson 100 - Search and Findall:")
text = "MMohamedAbdelfattah kkapaka44@gmail.com info@elzero.org"
# Search for two capital letters
my_search = re.search(r"[A-Z]{2}", text)
print("Search for [A-Z]{2}:", my_search)
if my_search:
    print("Span:", my_search.span())
    print("String:", my_search.string)
    print("Group:", my_search.group())

# Search for email
is_email = re.search(r"[A-Za-z0-9\.]+@[A-Za-z]+\.(com|net|org|info)", text)
if is_email:
    print("Valid email found:", is_email.group())
else:
    print("No valid email found")

# Findall for emails
emails = re.findall(r"[A-Za-z0-9\.]+@[A-Za-z]+\.(com|net|org|info)", text)
print("Findall emails:", emails)

# Interactive email validator
print("\nInteractive email validator:")
while True:
    email = input("Enter email (or 'exit' to quit): ").strip()
    if email.lower() == "exit":
        break
    valid_email = re.findall(r"[A-Za-z0-9\.]+@[A-Za-z]+\.(com|net|org|info)", email)
    if valid_email:
        print(f"Congratulations! Valid email: {valid_email[0]} 😍🎇🎉")
    else:
        print("Not a valid email 🎃🎃")
print("")
print("------------------------------------")
print("")

# Lesson 101 - Re Module Split and Sub
# split() splits text by pattern; sub() replaces matches
print("Lesson 101 - Split and Sub:")
text = "I love python"
print(f"Text: {text}")
print("Split by whitespace:", re.split(r"\s", text))  # ['I', 'love', 'python']
print("Split with maxsplit=1:", re.split(r"\s", text, maxsplit=1))  # ['I', 'love python']

article = "hello_world-iamhere _ studting_h"
print(f"Article: {article}")
split_words = re.split(r"[-_\s]", article)
print("Split by -, _, or space:", split_words)
# Print non-empty words with index
for i, word in enumerate(split_words, 1):
    if word:
        print(f"{i} => {word}")

# Replace -, _, or space with &
print("Sub -, _, or space with &:")
print(re.sub(r"[-_\s]", " & ", article))
print("")
print("------------------------------------")
print("")

# Lesson 102 - Group Trainings and Flags
# Advanced grouping and using flags like re.IGNORECASE
print("Lesson 102 - Group Trainings and Flags:")
text = "Email: Info@elzero.org, Website: HTTPS://WWW.ELZERO.COM"
# Email pattern with groups
email_pattern = r"([A-Za-z0-9\.]+)@([A-Za-z]+)\.([a-z]{2,})"
emails = re.findall(email_pattern, text, re.IGNORECASE)
print(f"Email pattern with groups: {email_pattern}")
print("Emails (username, domain, tld):", emails)

# URL pattern with flags
url_pattern = r"(https?)://(www\.)?(\w+)\.([a-z]{2,})"
urls = re.findall(url_pattern, text, re.IGNORECASE)
print(f"URL pattern: {url_pattern}")
print("URLs (protocol, www, domain, tld):", urls)
print("")
print("------------------------------------")
print("")

# Summary of Lessons 095 to 102
print("Summary:")
print("1 - Introduced regular expressions for pattern matching")
print("2 - Used quantifiers to control pattern repetition")
print("3 - Applied character classes to match specific characters")
print("4 - Implemented logical OR and escaping for flexible patterns")
print("5 - Grouped patterns for structured matches")
print("6 - Searched and found matches with re.search and re.findall")
print("7 - Split and replaced text with re.split and re.sub")
print("8 - Trained on grouping with flags like re.IGNORECASE")