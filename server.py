import jinja2
from flask import Flask, render_template, url_for, redirect, session, flash, request

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secretkeyyy'

app.jinja_env.undefined = jinja2.StrictUndefined

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=3001)