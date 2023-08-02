from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models import Athlete, Exercise
from app import db

athletes_blueprint = Blueprint("athletes", __name__)

@athletes_blueprint.route("/athletes")
def athletes():
    athletes = Athlete.query.all()
    return render_template("index.jinja", athletes = athletes)

# NEW
@athletes_blueprint.route("/athlete/<id>")
def show(id):
    athlete = Athlete.query.get(id)
    exercises = Exercise.query.join(Exercise).filter(Exercise.user_id == id)
    return render_template("athletes/show.jinja", athlete=athlete, exercises=exercises)
