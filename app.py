from flask import Flask, render_template
from canvasapi import Canvas
from datetime import datetime

app = Flask(__name__)

# Canvas API URL
API_URL = "https://canvas.pitt.edu/"
# Canvas API key
API_KEY = "13997~3pNoc4YCBSWPQllErzLhjhunsyf7Z4fEVvbJhdIWCp1WQSPwRA8nJp9n9ic8AUmq"
#Key and URL are hardcoded for now becasue we don't have the dev key, but later will have an Oauth2
#section where we get use the login page to redirect to canvas that the user logs into
#and canvas will send us an url with this API Key in it 

# Initialize a new Canvas object
canvas = Canvas(API_URL, API_KEY)
#185628
user = canvas.get_user(185628)
#Creates a User object, which is different from an Account object, from the canvasapi
#the argument it takes is the 6 digit user ID # that is unique to all canvas accounts

courses = user.get_courses()
#Initalizes a paginated list(you can itterate through it, but can't size it), of all ACTIVE courses the user has

todoList = []
#Initializes an empty list that we use forloops to fill
#This will end up being a list of dictionaries, where each dictionary is an assignment

for course in courses:
    assignments = course.get_assignments(bucket = 'unsubmitted', order_by = 'due_at')
    for assignment in assignments:
        dueDate = assignment.due_at
        #dueDate = [dueDate.day, dueDate.month, dueDate.year]
        todoList.append({"assName":assignment.name, "dueDate": dueDate, "className": course.name, "completed": False})
#loops over all active user courses then loops all assignments in that course and appends it to the list

#function to sort the list of dict before passing it into the list.html
for assignment in todoList:
    '''WIP'''

@app.route("/")#Default page
def home():
    return "Home"

@app.route("/list")#the list display
def main():
    return render_template('list.html', assignments=todoList)#takes in the list of dicts we made, so the javascript can interact with it
    #uses the render_template method, which is a built in method to the flask library to display
    #an html file that "we" made, this is where the javascript frontend gets called in our python program

@app.route("/login")#the login page, which doesn't do shit rn cause we don't have a dev key, theoretically it would do the Oauth2 redirection
def login_page():
    return render_template('login.html')