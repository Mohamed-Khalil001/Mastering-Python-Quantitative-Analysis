# Mastering Python - Lessons 133 to 140
# Topic: Introduction to Flask Web Framework
# This code covers key concepts from Lessons 133 to 140 of the "Mastering Python" course by Elzero Web School:
# - Lesson 133: Flask introduction and installation
# - Lesson 134: Flask first application
# - Lesson 135: Flask URL routing
# - Lesson 136: Flask HTTP methods (GET/POST)
# - Lesson 137: Flask templates (Jinja2)
# - Lesson 138: Flask static files (CSS/JS)
# - Lesson 139: Flask forms handling
# - Lesson 140: Flask redirect and errors
#
# Note: Install Flask using `pip install flask` before running this code.
# Run this file directly to start the Flask development server.

try:
    from flask import Flask, render_template, request, redirect, url_for, abort
except ImportError:
    print("Flask not installed. Run 'pip install flask' to use this code.")
    exit(1)

import os

# Lesson 133 - Flask Introduction and Installation
# Flask is a lightweight web framework for Python
print("Lesson 133 - Flask Introduction and Installation:")
print("Flask is a micro web framework for building web applications")
print("Install Flask with: pip install flask")
print("This code assumes Flask is installed")
print("")
print("------------------------------------")
print("")

# Lesson 134 - Flask First Application
# Create a basic Flask app
print("Lesson 134 - Flask First Application:")
app = Flask(__name__)


@app.route('/')
def home():
    return "Hello, Welcome to My First Flask App!"


print("Basic Flask app created. Visit http://127.0.0.1:5000/ to see it.")
print("")
print("------------------------------------")
print("")

# Lesson 135 - Flask URL Routing
# Define multiple routes for different URLs
print("Lesson 135 - Flask URL Routing:")


@app.route('/about')
def about():
    return "<h1>About Page</h1><p>This is the about page of our app.</p>"


@app.route('/user/<username>')
def user_profile(username):
    return f"<h1>Hello, {username}!</h1>"


@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f"<h1>Post ID: {post_id}</h1>"


print("Added routes: /about, /user/<username>, /post/<int:post_id>")
print("Try: http://127.0.0.1:5000/user/Ahmed or http://127.0.0.1:5000/post/42")
print("")
print("------------------------------------")
print("")

# Lesson 136 - Flask HTTP Methods (GET/POST)
# Handle GET and POST requests
print("Lesson 136 - Flask HTTP Methods (GET/POST):")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        return f"<h1>Logged in as {username}</h1>"
    return """
        <form method="post">
            <label>Username: <input type="text" name="username"></label>
            <input type="submit" value="Login">
        </form>
    """


print("Added /login route with GET/POST methods")
print("Visit http://127.0.0.1:5000/login to test the form")
print("")
print("------------------------------------")
print("")

# Lesson 137 - Flask Templates (Jinja2)
# Use Jinja2 templates for dynamic HTML
print("Lesson 137 - Flask Templates (Jinja2):")
# Create a templates folder and a sample template (index.html)
if not os.path.exists('templates'):
    os.makedirs('templates')
with open('templates/index.html', 'w') as f:
    f.write("""
        <!DOCTYPE html>
        <html>
        <head><title>{{ title }}</title></head>
        <body>
            <h1>Welcome, {{ username }}!</h1>
            <ul>
            {% for item in items %}
                <li>{{ item }}</li>
            {% endfor %}
            </ul>
        </body>
        </html>
    """)


@app.route('/template')
def template():
    return render_template('index.html', title="My App", username="Mohamed", items=['Python', 'Flask', 'Jinja2'])


print("Created templates/index.html and /template route")
print("Visit http://127.0.0.1:5000/template to see the Jinja2 template")
print("")
print("------------------------------------")
print("")

# Lesson 138 - Flask Static Files (CSS/JS)
# Serve static files like CSS and JS
print("Lesson 138 - Flask Static Files (CSS/JS):")
# Create a static folder and a sample CSS file (style.css)
if not os.path.exists('static'):
    os.makedirs('static')
with open('static/style.css', 'w') as f:
    f.write("""
        body {
            background-color: #f0f0f0;
            font-family: Arial, sans-serif;
        }
        h1 {
            color: #333;
        }
    """)

# Update index.html to include CSS
with open('templates/index.html', 'w') as f:
    f.write("""
        <!DOCTYPE html>
        <html>
        <head>
            <title>{{ title }}</title>
            <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
        </head>
        <body>
            <h1>Welcome, {{ username }}!</h1>
            <ul>
            {% for item in items %}
                <li>{{ item }}</li>
            {% endfor %}
            </ul>
        </body>
        </html>
    """)

print("Created static/style.css and updated /template to use CSS")
print("Visit http://127.0.0.1:5000/template to see styled page")
print("")
print("------------------------------------")
print("")

# Lesson 139 - Flask Forms Handling
# Handle form data with validation
print("Lesson 139 - Flask Forms Handling:")
# Create a registration form template (register.html)
with open('templates/register.html', 'w') as f:
    f.write("""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Register</title>
            <link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
        </head>
        <body>
            <h1>Register</h1>
            {% if error %}
                <p style="color: red;">{{ error }}</p>
            {% endif %}
            <form method="post">
                <label>Username: <input type="text" name="username"></label><br>
                <label>Password: <input type="password" name="password"></label><br>
                <input type="submit" value="Register">
            </form>
        </body>
        </html>
    """)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if not username or not password:
            return render_template('register.html', error="Username and password are required")
        if len(password) < 6:
            return render_template('register.html', error="Password must be at least 6 characters")
        return f"<h1>Registered: {username}</h1>"
    return render_template('register.html')


print("Created templates/register.html and /register route")
print("Visit http://127.0.0.1:5000/register to test the form")
print("")
print("------------------------------------")
print("")

# Lesson 140 - Flask Redirect and Errors
# Handle redirects and custom error pages
print("Lesson 140 - Flask Redirect and Errors:")


@app.route('/dashboard')
def dashboard():
    return redirect(url_for('home'))


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404 - Page Not Found</h1><p>Sorry, this page does not exist.</p>", 404


@app.route('/error')
def trigger_error():
    abort(404)


print("Added /dashboard (redirects to /) and custom 404 error page")
print("Visit http://127.0.0.1:5000/error to see 404 page")
print("")
print("------------------------------------")
print("")

# Summary of Lessons 133 to 140
print("Summary:")
print("1 - Introduced Flask and its installation")
print("2 - Created a basic Flask application")
print("3 - Implemented URL routing with dynamic parameters")
print("4 - Handled GET and POST HTTP methods")
print("5 - Used Jinja2 templates for dynamic HTML")
print("6 - Served static files (CSS/JS)")
print("7 - Handled forms with validation")
print("8 - Managed redirects and custom error pages")

# Run the Flask app
if __name__ == "__main__":
    print("Starting Flask server...")
    app.run(debug=True)
