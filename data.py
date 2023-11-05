from canvasapi import Canvas

# Canvas API URL
API_URL = "https://canvas.pitt.edu/"
# Canvas API key
API_KEY = "13997~BxWpzCZPNT346UNptXA0i8PuSPVCmQpLkjNbRljIwnOU1nQITQeSEgIODjBBkiI2"

# Initialize a new Canvas object
canvas = Canvas(API_URL, API_KEY)
#185628
account = canvas.get_account(185628)

courses = account.get_courses()

for course in courses:#loops over all user courses then loops all assignments in the course and makes a new assignment object
    assignments = course.get_assignments()
    for assignment in assignments:
        print(assignment)#generate a new assignment object based off of the canvas assignment