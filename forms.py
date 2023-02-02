from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SelectField, SubmitField
from wtforms.validators import DataRequired, InputRequired, Length

class TeamForm(FlaskForm):
    team_name = StringField("whats your team name called bruv?", [validators.InputRequired(), validators.Length(max=255, min=12)])
    submit = SubmitField('submit')
