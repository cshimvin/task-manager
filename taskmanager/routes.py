from flask import render_template
from taskmanager import app, db
# import the database schema models from models.py
from taskmanager.models import Category, Task
@app.route("/")
def home():
    return render_template("base.html")
