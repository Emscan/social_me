from flask import Flask
from db import db

friendships = db.Table('friendships', 
	friend_id1 = db.Column(db.Integer, db.ForeignKey='users.id'),
	friend_id2 = db.Column(db.Integer, db.ForeignKey='users.id'))

