from flask import Flask, render_template

'''from canvasapi import Canvas

# Canvas API URL
API_URL = "https://example.com"
# Canvas API key
API_KEY = "p@$$w0rd"

# Initialize a new Canvas object
canvas = Canvas(API_URL, API_KEY)'''

app = Flask(__name__)

@app.route("/")
def login_page():
    return render_template('login.html')