from flask import Flask, render_template, request, redirect, flash
from flask import Blueprint
from models import Exercise, Athlete
from app import db
import random

exercises_blueprint = Blueprint("exercises", __name__)

motivations = [
    "Take care of your body. It’s the only place you have to live.",
"Don't stop when you're tired. Stop when you're done.",
"I got 99 problems, but I'm going to the gym to ignore all of them",
"You did not wake up today to be mediocre",
"Don't tell people your plans, show them your results."]

@exercises_blueprint.route("/exercises")
def exercises():
    exercises = Exercise.query.all()
    return render_template("exercises/index.jinja", exercises=exercises)

@exercises_blueprint.route("/exercises/<id>")
def show_exercise(id):
    exercise = Exercise.query.get(id)
    return render_template("exercises/show.jinja", exercise=exercise)

@exercises_blueprint.route("/exercises/<id>/delete", methods=["POST"])
def delete_exercise(id):
    exercise = Exercise.query.get(id)
    db.session.delete(exercise)
    db.session.commit()
    return redirect("/exercises")

@exercises_blueprint.route("/exercises/new")
def add_exercise():
    athletes = Athlete.query.all()
    return render_template("exercises/form.jinja", athletes=athletes, exercise=None)

@exercises_blueprint.route("/exercises", methods=["POST"])
def create_exercise():
    athlete_id = request.form['athlete_id']
    name = request.form['name']
    sets = request.form['sets']
    reps = request.form['reps']
    completed = 'completed' in request.form

    exercise = Exercise(athlete_id=athlete_id, name=name, sets=sets, reps=reps, completed=completed)

    db.session.add(exercise)
    db.session.commit()
    return redirect('/exercises')

@exercises_blueprint.route("/exercises/<id>/edit")
def edit_exercise(id):
    exercise = Exercise.query.get(id)
    athletes = Athlete.query.all()
    return render_template("exercises/form.jinja", exercise=exercise, athletes=athletes)

@exercises_blueprint.route("/exercises/<id>", methods=['POST'])
def update_exercise(id):
    athlete_id = request.form['athlete_id']
    name = request.form['name']
    sets = request.form['sets']
    reps = request.form['reps']
    completed = 'completed' in request.form

    exercise = Exercise.query.get(id)

    exercise.name = name
    exercise.athlete_id = athlete_id
    exercise.sets = int(sets)
    exercise.reps = int(reps)
    exercise.completed = completed
    
    db.session.commit()
    return redirect("/exercises")

@exercises_blueprint.route("/exercises/<id>/toggle_completed", methods=['POST'])
def toggle_completed(id):
    exercise = Exercise.query.get(id)
    exercise.completed = not exercise.completed
    db.session.commit()
    if exercise.completed:
        flash(random.choice(motivations))
    return redirect("/exercises")
