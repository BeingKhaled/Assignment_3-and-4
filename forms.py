from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, TextAreaField, SubmitField
from wtforms.validators import InputRequired, Email

class DataCollectionForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
    student_number = StringField('Student Number', validators=[InputRequired()])
    email = StringField('Email Address', validators=[InputRequired(), Email()])
    grades = StringField('Grades Obtained in Courses', validators=[InputRequired()])
    satisfaction = SelectField('Overall Satisfaction with Academic Experience',
                               choices=[('verySatisfied', 'Very Satisfied'), ('satisfied', 'Satisfied'),
                                        ('neutral', 'Neutral'), ('dissatisfied', 'Dissatisfied'),
                                        ('veryDissatisfied', 'Very Dissatisfied')],
                               validators=[InputRequired()])
    suggestions = TextAreaField('Suggestions for Improvement', validators=[InputRequired()])
