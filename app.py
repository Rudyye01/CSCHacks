from flask import Flask, render_template

app = Flask(__name__)

sample_assignments = [
    {"due_date": "11-10", "class_name": "Math", "assignment_name": "Algebra Homework", "completed": False},
    {"due_date": "11-12", "class_name": "History", "assignment_name": "Research Paper", "completed": True},
    {"due_date": "11-15", "class_name": "Science", "assignment_name": "Lab Report", "completed": False},
    {"due_date": "11-18", "class_name": "English", "assignment_name": "Literature Essay", "completed": False},
    {"due_date": "11-20", "class_name": "Art", "assignment_name": "Painting Project", "completed": True},
]

@app.route("/")
def home():
    return "Home"

@app.route("/list")
def main():
    return render_template('list.html', assignments=sample_assignments)

@app.route("/login")
def login_page():
    return render_template('login.html')