# Mastering Python - Lessons 150 to 152
# Topic: Virtual Environments and Course Conclusion
# This code covers key concepts from Lessons 150 to 152 of the "Mastering Python" course by Elzero Web School:
# - Lesson 150: Virtual environments introduction and setup
# - Lesson 151: Managing packages in virtual environments
# - Lesson 152: Course conclusion and next steps
#
# Note: This code demonstrates commands for virtual environments.
# Some commands (e.g., venv creation) are shown as comments or print statements
# since they are typically run in the terminal, not in Python scripts.
# Ensure Python 3.3+ is installed for `venv`. Optionally, install `virtualenv` with:
# pip install virtualenv

import os
import sys
import subprocess
import pkg_resources

# # # _________________________________Lesson 150 _______________________
# # # --Virtual Environments => Introduction and Setup --
# # # ----------------------------------------------
# # # Virtual environments isolate Python projects
# # # Use `venv` to create isolated environments
# # # Commands: python -m venv env_name, activate, deactivate
# # # ----------------------------------------------
print("Lesson 150 - Virtual Environments Introduction and Setup:")
print("Virtual environments allow isolated Python environments for different projects")
print("Why use virtual environments?")
print("- Avoid package conflicts")
print("- Manage project-specific dependencies")
print("- Replicate environments across machines")
print("")
print("Using `venv` (built-in module):")
print("1. Create a virtual environment:")
print("   python -m venv myenv")
print("2. Activate the virtual environment:")
if sys.platform == "win32":
    print("   myenv\\Scripts\\activate (Windows)")
else:
    print("   source myenv/bin/activate (Linux/Mac)")
print("3. Deactivate:")
print("   deactivate")
print("")
print("Example: Creating a virtual environment programmatically")
venv_name = "test_env"
try:
    subprocess.run([sys.executable, "-m", "venv", venv_name], check=True)
    print(f"Virtual environment '{venv_name}' created")
except subprocess.CalledProcessError as e:
    print(f"Error creating virtual environment: {e}")
print("")
print("------------------------------------")
print("")

# # # _________________________________Lesson 151 _______________________
# # # --Virtual Environments => Managing Packages --
# # # ----------------------------------------------
# # # Use pip to install, list, and save packages
# # # Commands: pip install, pip list, pip freeze
# # # Save dependencies to requirements.txt
# # # ----------------------------------------------
print("Lesson 151 - Managing Packages in Virtual Environments:")
print("After activating a virtual environment, use `pip` to manage packages")
print("Example commands (run in terminal after activating):")
print("1. Install a package:")
print("   pip install requests")
print("2. List installed packages:")
print("   pip list")
print("3. Save dependencies to a file:")
print("   pip freeze > requirements.txt")
print("4. Install dependencies from a file:")
print("   pip install -r requirements.txt")
print("")
print("Example: Check installed packages programmatically")


def list_installed_packages():
    """List all installed packages in the current Python environment."""
    installed = sorted(
        [f"{pkg.key}=={pkg.version}" for pkg in pkg_resources.working_set])
    return installed


print("Packages in current environment:")
for pkg in list_installed_packages()[:5]:  # Limit to 5 for brevity
    print(f"- {pkg}")
print("")
print("Example: Simulate installing a package in a virtual environment")
requirements_file = "requirements.txt"
with open(requirements_file, "w") as f:
    f.write("requests==2.31.0\n")
print(f"Created {requirements_file} with 'requests==2.31.0'")
print("To install in a virtual environment:")
print(
    f"1. Activate: source {venv_name}/bin/activate (Linux/Mac) or {venv_name}\\Scripts\\activate (Windows)")
print(f"2. Run: pip install -r {requirements_file}")
print("")
print("------------------------------------")
print("")

# # # _________________________________Lesson 152 _______________________
# # # --Course => Conclusion and Next Steps --
# # # ----------------------------------------------
# # # Wrap up the Mastering Python course
# # # Suggest further learning paths
# # # Review key topics covered
# # # ----------------------------------------------
print("Lesson 152 - Course Conclusion and Next Steps:")
print("Congratulations on completing the Mastering Python course!")
print("Key topics covered:")
print("- Basics: Variables, loops, functions")
print("- Advanced: OOP, decorators, generators")
print("- Databases: SQLite")
print("- Web: Flask, web scraping")
print("- Numerical: NumPy")
print("- Testing: unittest")
print("- Environments: Virtual environments")
print("")
print("Next steps:")
print("- Build real-world projects (e.g., web apps, data analysis)")
print("- Explore advanced libraries: Pandas, Django, FastAPI")
print("- Contribute to open-source")
print("- Learn about deployment (e.g., Docker, Heroku)")
print("")
print("---------------------------------------------------------------------------------------------------------")
print("Example: Check Python version and environment:")
print(f"Python: {sys.version}")
print(f"Current environment: {sys.executable}")
print("")
print("")
print("------------------------------------")

# Summary of Lessons
print("Summary:")
print("1 - Introduced virtual environments for project isolation")
print("2 - Demonstrated package management with pip")
print("3 - Concluded the course with next steps")
print("")
print("To clean up, remove the test environment:")
print(f"rm -rf {venv_name} (Linux/Mac) or f"rmdir / s {venv_name}(Windows)")

if __name__ == "__main__":
    print("Script executed directly. Use terminal for virtual environment commands.")