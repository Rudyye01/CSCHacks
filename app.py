import re
from datetime import datetime

from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    