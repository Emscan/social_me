import bcrypt
from datetime import datetime
from db import db
from flask import abort, Blueprint, flash, Flask, g, Markup, redirect, render_template, request, session
from functools import wraps
from helpers import *
from models import *
from sqlalchemy.exc import IntegrityError, InvalidRequestError
from blueprints import *

app = Flask(__name__)
app.config.from_object('config')

db.create_all()

def gen_csrf_token():
	if '_csrf_token' not in session:
		session['_csrf_token'] = bcrypt.gensalt()
	return session['_csrf_token']

def csrf_helper():
	token = gen_csrf_token()
	return Markup('<input type="hidden" name="_csrf_token" value="{0}" />'.format(token))

app.jinja_env.globals['csrf_helper'] = csrf_helper
app.jinja_env.globals['fb_oauth_link'] = 'https://www.facebook.com/dialog/oauth?client_id={0}&redirect_uri={1}'.format(app.config['FB_APP_ID'], app.config['FB_REDIRECT_URI'])

@app.before_request
def csrf_protect():
	if request.method == 'POST':
		token = session.pop('_csrf_token', None)
		form_token = request.form.get('_csrf_token')
		if not token or not form_token or token != form_token:
			abort(403)

@app.route('/homepage')
@logged_in
def homepage():
	return render_template('homepage.html')

@app.route('/index')
def index():
	user = current_user()
	username = None
	if user:
		username = User.username
	return render_template('index.html', username=username, current_user=user)

app.register_blueprint(auth.auth, session=session, g=g)
app.register_blueprint(user.user, session=session, g=g)

if __name__ == '__main__':
	app.run()
