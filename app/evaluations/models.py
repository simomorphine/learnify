from flask_sqlalchemy import SQLAlchemy
#need to import db here

class Evaluation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    grade = db.Column(db.String(10), nullable=False)
    number_of_exercises = db.Column(db.Integer, nullable=False)
    instructions = db.Column(db.Text, nullable=True)

    # Relationship to File model
    files = db.relationship('File', backref='evaluation', lazy=True)

class File(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255), nullable=False)
    filepath = db.Column(db.String(255), nullable=False)
    evaluation_id = db.Column(db.Integer, db.ForeignKey('evaluation.id'), nullable=False)

    def __repr__(self):
        return f'<File {self.filename}>'
