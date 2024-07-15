from flask_wtf import FlaskForm
from wtforms import StringField, DateField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class LeaveRequestForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    start_date = DateField('Start Date', validators=[DataRequired()])
    end_date = DateField('End Date', validators=[DataRequired()])
    reason = TextAreaField('Reason', validators=[DataRequired()])
    submit = SubmitField('Request Leave')
