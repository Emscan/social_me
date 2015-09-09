from datetime import datetime
from db import db
from flask import Blueprint, flash, Flask, g, redirect, render_template, request, session
from functools import wraps
from models import *
from sqlalchemy.exc import IntegrityError, InvalidRequestError
from blueprints import *

app = Flask(__name__)
app.config.from_object('config')

db.create_all()


def logged_in(func):
	@wraps(func)
	def decorated(*args, **kwargs):
		if current_user():
			return func(*args, **kwargs)
		else:
			flash('You must be logged in!')
			return redirect('/login')

@app.route('/friends')
def friends():
	pass


@app.route('/homepage')
def homepage():
	user = current_user()
	username = user.username
	return render_template('/homepage')

@app.route('/index')
def index():
	user = current_user()
	username = None
	if user:
		username = user.username
	return render_template('index.html', username=username, current_user=user)

@app.route('/comments')
def messages():
	 #TODO, make template
	 body = db.Column(db.String(1000), nullable=False)

@app.route('/posts', methods=['POST'])
def post():
	pass
	#TODO, make template

@app.route('/shares')
def shares():
	pass

@app.route('/tags')
def tags():
	pass

app.register_blueprint(auth.auth, session=session, g=g)

if __name__ == '__main__':
	app.run()
