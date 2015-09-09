from comments import *
from posts import *
from shares import *
from tags import *
from users import *


def current_user():
	current_user = g.get('current_user')
	if not current_user:
		token = session.get('token')
		if token:
			current_user = User.from_token(token)
	g.current_user = current_user
	return current_user