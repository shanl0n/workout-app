from app import db

class Athlete(db.Model):
    __tablename__ = "athletes"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))

    def __repr__(self):
        return f"<Name: {self.id}: {self.name}>"

class Exercise(db.Model):
    __tablename__ = "exercises"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    sets = db.Column(db.Integer)
    reps = db.Column(db.Integer)
    completed = db.Column(db.Boolean, default=False)
    athlete_id = db.Column(db.Integer, db.ForeignKey('athletes.id'))

    def __repr__(self):
        return f"<Exercise: {self.id}: {self.name}>"
    
def remove_exercise(id):
    exercise = Exercise.query.get(id)
    db.session.delete(exercise)
    db.session.commit()