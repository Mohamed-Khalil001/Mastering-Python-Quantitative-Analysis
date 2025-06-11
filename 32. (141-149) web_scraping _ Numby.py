# Mastering Python - Lessons 141 to 149
# Topic: Web Scraping and Advanced NumPy
# This code covers key concepts from Lessons 141 to 149 of the "Mastering Python" course by Elzero Web School:
# - Lesson 141: Web scraping introduction and installation
# - Lesson 142: Web scraping with requests and BeautifulSoup
# - Lesson 143: Navigating HTML with BeautifulSoup
# - Lesson 144: Extracting data from web pages
# - Lesson 145: NumPy data types and attributes
# - Lesson 146: NumPy array creation methods
# - Lesson 147: NumPy array reshaping
# - Lesson 148: NumPy array basic operations
# - Lesson 149: NumPy array indexing and slicing
#
# Note: Install required libraries using:
# pip install requests beautifulsoup4 numpy

import sys
try:
    import requests
    from bs4 import BeautifulSoup
    import numpy as np
except ImportError as e:
    print(
        f"Missing library: {e}. Install with 'pip install requests beautifulsoup4 numpy'")
    sys.exit(1)

# Lesson 141 - Web Scraping Introduction and Installation
# Web scraping extracts data from websites
print("Lesson 141 - Web Scraping Introduction and Installation:")
print("Web scraping retrieves data from HTML pages using tools like requests and BeautifulSoup")
print("Install libraries with: pip install requests beautifulsoup4")
print("This code assumes libraries are installed")
print("")
print("------------------------------------")
print("")

# Lesson 142 - Web Scraping with requests and BeautifulSoup
# Fetch a webpage and parse its HTML
print("Lesson 142 - Web Scraping with requests and BeautifulSoup:")
url = "https://example.com"  # Simple example website
try:
    response = requests.get(url, timeout=5)
    response.raise_for_status()  # Check for HTTP errors
    soup = BeautifulSoup(response.text, 'html.parser')
    print("Fetched and parsed:", soup.title.text)
except requests.RequestException as e:
    print(f"Error fetching URL: {e}")

print("")
print("------------------------------------")
print("")

# Lesson 143 - Navigating HTML with BeautifulSoup
# Traverse HTML tags and attributes
print("Lesson 143 - Navigating HTML with BeautifulSoup:")
# Sample HTML for demonstration
sample_html = """
<html>
    <body>
        <div class="content">
            <h1>Main Title</h1>
            <p class="intro">Welcome to scraping!</p>
            <p>Second paragraph</p>
        </div>
    </body>
</html>
"""
soup = BeautifulSoup(sample_html, 'html.parser')
print("Title:", soup.h1.text)
print("First paragraph (class=intro):", soup.find('p', class_='intro').text)
print("All paragraphs:", [p.text for p in soup.find_all('p')])
print("")
print("------------------------------------")
print("")

# Lesson 144 - Extracting Data from Web Pages
# Extract specific data from a real webpage
print("Lesson 144 - Extracting Data from Web Pages:")
# Using example.com again (simple structure)
try:
    response = requests.get(url, timeout=5)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = [a.get('href') for a in soup.find_all('a', href=True)]
    print("Links found on example.com:", links[:5])  # Limit to 5 for brevity
except requests.RequestException as e:
    print(f"Error fetching URL: {e}")

# Example: Store scraped data in NumPy array
if links:
    links_array = np.array(links[:5])  # Convert to NumPy array
    print("Links as NumPy array:", links_array)
print("")
print("------------------------------------")
print("")

# Lesson 145 - NumPy Data Types and Attributes
# Explore NumPy array data types and attributes
print("Lesson 145 - NumPy Data Types and Attributes:")
arr = np.array([1, 2, 3, 4, 5])
print("Array:", arr)
print("Data type:", arr.dtype)
print("Shape:", arr.shape)
print("Size (total elements):", arr.size)
print("Number of dimensions:", arr.ndim)

arr_float = np.array([1.1, 2.2, 3.3], dtype=np.float32)
print("\nFloat array:", arr_float)
print("Data type:", arr_float.dtype)
print("")
print("------------------------------------")
print("")

# Lesson 146 - NumPy Array Creation Methods
# Create arrays using various NumPy methods
print("Lesson 146 - NumPy Array Creation Methods:")
zeros = np.zeros((2, 3))
ones = np.ones((2, 2))
full = np.full((2, 2), 7)
arange = np.arange(0, 10, 2)
linspace = np.linspace(0, 1, 5)
print("Zeros (2x3):\n", zeros)
print("Ones (2x2):\n", ones)
print("Full (2x2, value=7):\n", full)
print("Arange (0 to 10, step=2):", arange)
print("Linspace (0 to 1, 5 points):", linspace)
print("")
print("------------------------------------")
print("")

# Lesson 147 - NumPy Array Reshaping
# Reshape arrays to different dimensions
print("Lesson 147 - NumPy Array Reshaping:")
arr = np.array([1, 2, 3, 4, 5, 6])
reshaped = arr.reshape(2, 3)
flattened = reshaped.flatten()
print("Original array:", arr)
print("Reshaped (2x3):\n", reshaped)
print("Flattened:", flattened)
print("Reshape to (3x2):\n", arr.reshape(3, 2))
try:
    arr.reshape(2, 4)  # Will raise error (invalid shape)
except ValueError as e:
    print("Error reshaping:", e)
print("")
print("------------------------------------")
print("")

# Lesson 148 - NumPy Array Basic Operations
# Perform arithmetic and statistical operations
print("Lesson 148 - NumPy Array Basic Operations:")
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print("Array 1:", arr1)
print("Array 2:", arr2)
print("Addition:", arr1 + arr2)
print("Multiplication:", arr1 * arr2)
print("Square root of arr1:", np.sqrt(arr1))
print("Mean of arr1:", np.mean(arr1))
print("Max of arr2:", np.max(arr2))
print("")
print("------------------------------------")
print("")

# Lesson 149 - NumPy Array Indexing and Slicing
# Access and modify array elements
print("Lesson 149 - NumPy Array Indexing and Slicing:")
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("2D array:\n", arr)
print("Element at [1,2]:", arr[1, 2])
print("First row:", arr[0, :])
print("Second column:", arr[:, 1])
print("Slice [0:2, 1:3]:\n", arr[0:2, 1:3])
# Modify elements
arr[0, 0] = 10
print("Modified array:\n", arr)
print("")
print("------------------------------------")
print("")

# Summary of Lessons 141 to 149
print("Summary:")
print("1 - Introduced web scraping with requests and BeautifulSoup")
print("2 - Fetched and parsed web pages")
print("3 - Navigated HTML structures")
print("4 - Extracted and stored data in NumPy arrays")
print("5 - Explored NumPy data types and attributes")
print("6 - Created arrays with various methods")
print("7 - Reshaped arrays to different dimensions")
print("8 - Performed basic arithmetic and statistical operations")
print("9 - Indexed and sliced NumPy arrays")
