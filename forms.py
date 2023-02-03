from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SelectField, SubmitField, validators, BooleanField, TextAreaField
from wtforms.validators import DataRequired, InputRequired, Length

class TeamForm(FlaskForm):
    team_name = StringField("whats your team name called bruv?", [validators.InputRequired(), validators.Length(max=255, min=12)])
    submit = SubmitField('submit')

class ProjectForm(FlaskForm):
    project_name = StringField("Project Name", [validators.InputRequired(), validators.Length(max=255, min=12)])
    description = TextAreaField("Project Description", [validators.Length(max=500, min=12)])
    completed = BooleanField('Completed?')
    team_selection = SelectField("team")
    submit = SubmitField("Submit")

    def update_teams(self, teams):
        self.team_selection.choices = [ (te.id, te.team_name) for te in teams ]
        print(self.team_selection)

class UserForm(FlaskForm):
    username = StringField('username',[validators.InputRequired()])
    password = StringField('password',[validators.InputRequired()])
    submit = SubmitField()
