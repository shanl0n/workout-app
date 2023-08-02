from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# Import all models

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://seanhanlon@localhost:5432/workout_assistant"
app.config["SQLALCHEMY_ECHO"] = True
db = SQLAlchemy(app)
migrate = Migrate(app, db)
app.secret_key = 'dont tell anyone'

# Import and Register Controllers
from controllers.athlete_controller import athletes_blueprint
from controllers.exercise_controller import exercises_blueprint

app.register_blueprint(athletes_blueprint)
app.register_blueprint(exercises_blueprint)

@app.route("/")
def home():
    return render_template("index.jinja")

if __name__ == '__main__':
    app.run(debug=True)