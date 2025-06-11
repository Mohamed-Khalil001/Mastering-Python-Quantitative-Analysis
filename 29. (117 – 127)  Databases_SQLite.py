# Mastering Python - Lessons 117 to 127
# Topic: SQLite Database Operations in Python
# This code covers key concepts from Lessons 117 to 127 of the "Mastering Python" course by Elzero Web School:
# - Lesson 117: Introduction to databases
# - Lesson 118: SQLite create database and connect
# - Lesson 119: SQLite insert data
# - Lesson 120: SQLite retrieve data
# - Lesson 121: SQLite training on everything
# - Lesson 122: SQLite update and delete
# - Lesson 123: SQLite create skills app (Part 1)
# - Lesson 124: SQLite create skills app (Part 2)
# - Lesson 125: SQLite create skills app (Part 3)
# - Lesson 126: SQLite create skills app (Part 4)
# - Lesson 127: SQLite create skills app (Part 5)

import sqlite3

# Lesson 117 - Database Introduction
# Databases store organized data in tables with columns
print("Lesson 117 - Database Introduction:")
print("Databases organize data in tables (e.g., users, skills)")
print("Columns define data types (e.g., text, integer)")
print("SQLite is a lightweight database stored in a single file")
print("Browse SQLite files at: http://sqlitebrowser.org/")
print("")
print("------------------------------------")
print("")

# Lesson 118 - SQLite Create Database and Connect
# Connect, execute, and close database operations
print("Lesson 118 - SQLite Create Database and Connect:")
db = sqlite3.connect("dbskills.db")
print("Connected to dbskills.db")
cr = db.cursor()
cr.execute("CREATE TABLE IF NOT EXISTS users (user_name TEXT, id INTEGER)")
cr.execute("CREATE TABLE IF NOT EXISTS skills (user_name TEXT, id INTEGER, skill TEXT, progress INTEGER)")
db.commit()
db.close()
print("Tables created and connection closed")
print("")
print("------------------------------------")
print("")

# Lesson 119 - SQLite Insert Data
# Insert data using cursor and commit changes
print("Lesson 119 - SQLite Insert Data:")
db = sqlite3.connect("dbskills.db")
cr = db.cursor()
cr.execute("DELETE FROM users")
cr.execute("DELETE FROM skills")
mylist = ["Ahmed", "Sayed", "Khaled", "Magdy", "Hany", "Fady", "MAHA", "Soha"]
for idd, user in enumerate(mylist, 1):
    cr.execute(f"INSERT INTO users (user_name, id) VALUES ('{user}', {idd})")
db.commit()
print("Inserted users:", mylist)
db.close()
print("")
print("------------------------------------")
print("")

# Lesson 120 - SQLite Retrieve Data
# Fetch data using fetchone, fetchall, and fetchmany
print("Lesson 120 - SQLite Retrieve Data:")
db = sqlite3.connect("dbskills.db")
cr = db.cursor()
cr.execute("SELECT user_name FROM users")
print("Fetchone (first 3):")
print(cr.fetchone())
print(cr.fetchone())
print(cr.fetchone())
print("\nFetchall (remaining):")
print(cr.fetchall())
cr.execute("SELECT user_name FROM users")
print("\nFetchmany (2):")
print(cr.fetchmany(2))
cr.execute("SELECT user_name, id FROM users")
print("\nFetchone with multiple columns (first 3):")
print(cr.fetchone())
print(cr.fetchone())
print(cr.fetchone())
print("\nFetchall (remaining):")
print(cr.fetchall())
cr.execute("SELECT user_name, id FROM users")
print("\nFetchmany with multiple columns (2):")
print(cr.fetchmany(2))
db.commit()
db.close()
print("")
print("------------------------------------")
print("")

# Lesson 121 - SQLite Training on Everything

# Comprehensive database operations
print("Lesson 121 - SQLite Training on Everything:")


def get_all_users():
    try:
        db = sqlite3.connect("dbskills.db")
        print("Successfully connected to database")
        cr = db.cursor()
        cr.execute("SELECT * FROM users")
        result = cr.fetchall()
        print(f"Database has {len(result)} users")
        for row in result:
            print(f"User name => {row[0]:<10} User ID => {row[1]}")
    except sqlite3.Error as er:
        print(f"Error reading data: {er}")
    finally:
        if db:
            db.close()
            print("Database connection closed")


get_all_users()
print("")
print("------------------------------------")
print("")

# Lesson 122 - SQLite Update and Delete
# Update and delete records in the database
print("Lesson 122 - SQLite Update and Delete:")
db = sqlite3.connect("dbskills.db")
cr = db.cursor()
cr.execute("UPDATE users SET user_name = 'Mohamed' WHERE id = 1")
cr.execute("UPDATE users SET user_name = 'Omar' WHERE id = 2")
cr.execute("UPDATE users SET user_name = 'Ahmed' WHERE id = 3")
cr.execute("DELETE FROM users WHERE id = 8")
cr.execute("SELECT * FROM users")
print("Updated and deleted users:", cr.fetchall())
db.commit()
db.close()
print("")
print("------------------------------------")
print("")

# Lesson 123 - SQLite Create Skills App (Part 1)
# Start building a skills management app
print("Lesson 123 - SQLite Create Skills App (Part 1):")
db = sqlite3.connect("app.db")
cr = db.cursor()
cr.execute("CREATE TABLE IF NOT EXISTS users (user_id INTEGER, user_name TEXT)")
cr.execute(
    "CREATE TABLE IF NOT EXISTS skills (skill TEXT, progress INTEGER, user_id INTEGER)")
ud = 2  # Default user ID
input_message = """
What do you want to do?
"s" => Show all skills
"a" => Add new skill
"d" => Delete a skill
"u" => Update skill progress
"q" => Quit the app
Choose option:
"""
command_list = ["s", "a", "d", "u", "q"]


def show_all_skills():
    """Display all skills for the current user."""
    cr.execute(f"SELECT * FROM skills WHERE user_id = {ud}")
    result = cr.fetchall()
    print(f"You have {len(result)} skills")
    if result:
        for row in result:
            print(f"Skill => {row[0]:<20} | Progress => {row[1]:>3}")
    else:
        print("No skills found for this user")
    db.commit()


def add_skill(sk: str = None):
    """Add a new skill to the database."""
    if sk is None:
        sk = input("What skill would you like to add? ").strip().capitalize()
    cr.execute(
        f"SELECT skill FROM skills WHERE skill = '{sk}' AND user_id = {ud}")
    result = cr.fetchone()
    if result is None:
        pr = input("Enter skill's progress: ").strip()
        if pr.isdigit():
            cr.execute(
                f"INSERT INTO skills (skill, progress, user_id) VALUES ('{sk}', {pr}, {ud})")
            print(f"{sk} skill added 📌✅")
        else:
            print("Progress must be a number")
    else:
        print(f"{sk} skill already exists, you can't add it 🎃😪")
        upp = input("Do you want to update it? (Y/N): ").strip().capitalize()
        if upp == 'Y':
            update_skill(sk)
        else:
            print("OK as you want 💜")
    db.commit()


def delete_skill():
    """Delete a skill from the database."""
    sk = input("What skill would you like to delete? ").strip().capitalize()
    cr.execute(f"DELETE FROM skills WHERE skill = '{sk}' AND user_id = {ud}")
    if cr.rowcount > 0:
        print(f"{sk} skill deleted 🗑️")
    else:
        print(f"{sk} skill not found 🎃")
    db.commit()


def update_skill(sk: str = None):
    """Update the progress of an existing skill."""
    if sk is None:
        sk = input("What skill would you like to update? ").strip().capitalize()
    cr.execute(
        f"SELECT skill FROM skills WHERE skill = '{sk}' AND user_id = {ud}")
    result = cr.fetchone()
    if result is not None:
        pr = input("Enter new skill's progress: ").strip()
        if pr.isdigit():
            cr.execute(
                f"UPDATE skills SET progress = {pr} WHERE skill = '{sk}' AND user_id = {ud}")
            print(f"{sk} skill updated ✳♻✅")
        else:
            print("Progress must be a number")
    else:
        print(f"{sk} skill does not exist, want to add it? 🎃😪")
        upp = input("Add it? (Y/N): ").strip().capitalize()
        if upp == 'Y':
            add_skill(sk)
        else:
            print("OK as you want 💜")
    db.commit()


def quit_the_app():
    """Save changes and close the database connection."""
    db.commit()
    db.close()
    print("App closed 👋")


print("Skills App initialized")
print("")
print("------------------------------------")
print("")

# Lesson 124 - SQLite Create Skills App (Part 2)
# Add input validation and error handling
print("Lesson 124 - SQLite Create Skills App (Part 2):")


def run_skills_app():
    """Run the skills app with input validation."""
    while True:
        try:
            option = input(input_message).lower().strip()
            if option not in command_list:
                print(f"'{option}' is not a valid command.")
                continue
            if option == "s":
                show_all_skills()
            elif option == "a":
                add_skill()
            elif option == "d":
                delete_skill()
            elif option == "u":
                update_skill()
            elif option == "q":
                quit_the_app()
                break
        except KeyboardInterrupt:
            print("\nApp interrupted, closing...")
            quit_the_app()
            break
        except Exception as e:
            print(f"Error occurred: {e}")


print("Running Skills App with input validation")
db = sqlite3.connect("app.db")
cr = db.cursor()
run_skills_app()
print("")
print("------------------------------------")
print("")

# Lesson 125 - SQLite Create Skills App (Part 3)
# Add user management
print("Lesson 125 - SQLite Create Skills App (Part 3):")
db = sqlite3.connect("app.db")
cr = db.cursor()
cr.execute("INSERT OR IGNORE INTO users (user_id, user_name) VALUES (2, 'Mohamed')")
db.commit()
print("User Mohamed (ID: 2) added to users table")
db.close()
print("")
print("------------------------------------")
print("")

# Lesson 126 - SQLite Create Skills App (Part 4)
# Enhance app with skill progress validation
print("Lesson 126 - SQLite Create Skills App (Part 4):")


def add_skill(sk: str = None):
    """Add a new skill with progress validation (0-100)."""
    if sk is None:
        sk = input("What skill would you like to add? ").strip().capitalize()
    cr.execute(
        f"SELECT skill FROM skills WHERE skill = '{sk}' AND user_id = {ud}")
    result = cr.fetchone()
    if result is None:
        pr = input("Enter skill's progress (0-100): ").strip()
        if pr.isdigit() and 0 <= int(pr) <= 100:
            cr.execute(
                f"INSERT INTO skills (skill, progress, user_id) VALUES ('{sk}', {pr}, {ud})")
            print(f"{sk} skill added 📌✅")
        else:
            print("Progress must be a number between 0 and 100")
    else:
        print(f"{sk} skill already exists, you can't add it 🎃😪")
        upp = input("Do you want to update it? (Y/N): ").strip().capitalize()
        if upp == 'Y':
            update_skill(sk)
        else:
            print("OK as you want 💜")
    db.commit()


def update_skill(sk: str = None):
    """Update skill progress with validation (0-100)."""
    if sk is None:
        sk = input("What skill would you like to update? ").strip().capitalize()
    cr.execute(
        f"SELECT skill FROM skills WHERE skill = '{sk}' AND user_id = {ud}")
    result = cr.fetchone()
    if result is not None:
        pr = input("Enter new skill's progress (0-100): ").strip()
        if pr.isdigit() and 0 <= int(pr) <= 100:
            cr.execute(
                f"UPDATE skills SET progress = {pr} WHERE skill = '{sk}' AND user_id = {ud}")
            print(f"{sk} skill updated ✳♻✅")
        else:
            print("Progress must be a number between 0 and 100")
    else:
        print(f"{sk} skill does not exist, want to add it? 🎃😪")
        upp = input("Add it? (Y/N): ").strip().capitalize()
        if upp == 'Y':
            add_skill(sk)
        else:
            print("OK as you want 💜")
    db.commit()


print("Skills App with progress validation (0-100)")
db = sqlite3.connect("app.db")
cr = db.cursor()
run_skills_app()
print("")
print("------------------------------------")
print("")

# Lesson 127 - SQLite Create Skills App (Part 5)
# Finalize app with user selection
print("Lesson 127 - SQLite Create Skills App (Part 5):")


def select_user():
    """Select a user from the database."""
    db = sqlite3.connect("app.db")
    cr = db.cursor()
    cr.execute("SELECT user_id, user_name FROM users")
    users = cr.fetchall()
    if not users:
        print("No users found. Adding default user...")
        cr.execute("INSERT INTO users (user_id, user_name) VALUES (1, 'Default')")
        db.commit()
        db.close()
        return 1
    print("Available users:")
    for user in users:
        print(f"ID: {user[0]}, Name: {user[1]}")
    while True:
        try:
            user_id = int(input("Enter user ID: "))
            cr.execute(f"SELECT user_id FROM users WHERE user_id = {user_id}")
            if cr.fetchone():
                db.close()
                return user_id
            print("Invalid user ID")
        except ValueError:
            print("Please enter a valid number")


db = sqlite3.connect("app.db")
cr = db.cursor()
ud = select_user()
print(f"Selected user ID: {ud}")
run_skills_app()
db.close()
print("")
print("------------------------------------")
print("")

# Summary of Lessons 117 to 127
print("Summary:")
print("1 - Introduced databases and SQLite")
print("2 - Created and connected to SQLite database")
print("3 - Inserted data into tables")
print("4 - Retrieved data using fetchone, fetchall, fetchmany")
print("5 - Trained on comprehensive database operations")
print("6 - Updated and deleted records")
print("7 - Built a skills management app with CRUD operations")
print("8 - Enhanced app with input validation")
print("9 - Added user management")
print("10 - Improved progress validation")
print("11 - Finalized app with user selection")
