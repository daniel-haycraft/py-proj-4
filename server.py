import jinja2
from flask import Flask, render_template, url_for, redirect, session, flash, request
from forms import TeamForm, ProjectForm, UserForm
from model import User, Team, Project, connect_to_db, db


app = Flask(__name__)


app.secret_key = 'my-py'
app.jinja_env.undefined = jinja2.StrictUndefined

USER_ID =1

@app.route('/add-user', methods=['GET', 'POST'])
def add_user():
    form = UserForm()
    team_form = TeamForm()
    project_form = ProjectForm()
    if form.validate_on_submit():
        with app.app_context():
            username = form.username.data
            password = form.password.data
            new_user = User(username, password)
            db.session.add(new_user)
            db.session.commit()
        return render_template('home.html', form = form, team_form = team_form, project_form = project_form)
    else:
        return redirect(url_for('home'))


@app.route('/')
def home():
    form = UserForm()
    team_form = TeamForm()
    project_form = ProjectForm()
    with app.app_context():
        project_form.update_teams(Team.query.filter_by(user_id = USER_ID).all())
    # project_form.update_teams(User.query.get(user_id).teams)
    return render_template('home.html', team_form = team_form, project_form = project_form, form = form)

@app.route('/add-team', methods=['GET', 'POST'])
def add_team():
    project_form = ProjectForm()
    team_form = TeamForm()
    if team_form.validate_on_submit():
        with app.app_context():
            team_name = team_form.team_name.data
            new_team = Team(team_name, USER_ID)
            db.session.add(new_team)
            db.session.commit()
        return render_template('home.html', team_form = team_form, project_form = project_form)
    else:
        return redirect(url_for('home'))

@app.route('/add-project', methods=[ 'POST'])
def add_project():
    project_form = ProjectForm()
    team_form = TeamForm()
    with app.app_context():
        project_form.update_teams(Team.query.filter_by(user_id = USER_ID).all())
    if project_form.validate_on_submit():
        with app.app_context():
            project_name = project_form.team_name.data
            description = project_form.description.data
            completed = project_form.completed.data
            new_project = Project(project_name, description, completed, team_id)
            db.session.add(new_project)
            db.session.commit()
        return render_template('home.html', project_form = project_form, team_form = team_form)
    else:
        return redirect(url_for('home'))


if __name__ == "__main__":
    connect_to_db(app)
    app.run(debug=True, host="localhost", port=3002)