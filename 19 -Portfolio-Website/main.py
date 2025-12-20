# main.py
from flask import Flask

app = Flask(__name__)

home_page = """
<h1>Welcome to My Portfolio</h1>
<p>This is a simple Flask website.</p>
<a href="/about">About</a> | <a href="/projects">Projects</a>
"""

about_page = """
<h1>About Me</h1>
<p>Hello! I'm learning Python and building cool projects.</p>
<a href="/">Home</a> | <a href="/projects">Projects</a>
"""

projects_page = """
<h1>My Projects</h1>
<ul>
    <li>Weather App</li>
    <li>News Scraper</li>
    <li>File Organizer</li>
    <li>Image Resizer</li>
    <li>Expense Tracker</li>
    <li>Email Sender</li>
    <li>Mini Search Engine</li>
    <li>Markdown to HTML Converter</li>
</ul>
<a href="/">Home</a> | <a href="/about">About</a>
"""

@app.route("/")
def home():
    return home_page

@app.route("/about")
def about():
    return about_page

@app.route("/projects")
def projects():
    return projects_page

if __name__ == "__main__":
    app.run(debug=True)
