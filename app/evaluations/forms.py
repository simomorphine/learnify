from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, FileField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class EvaluationForm(FlaskForm):
    grade = SelectField('Grade', choices=[
        ('1apic', '1apic'),
        ('2apic', '2apic'),
        ('3apic', '3apic'),
        ('TC', 'TC'),
        ('1bac', '1bac'),
        ('2bac', '2bac')
    ], validators=[DataRequired()])
    
    file_uploads = FileField('Upload Files', multiple=True)
    number_of_exercises = IntegerField('Number of Exercises', validators=[DataRequired(), NumberRange(min=1)])
    
    additional_files = FileField('Add More Files', multiple=True)
    instructions = TextAreaField('Instructions', description='Add one or more instructions.')
    
    submit = SubmitField('Submit')
