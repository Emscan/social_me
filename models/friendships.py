from flask import Flask
from db import db

friendships = db.Table('friendships', 
	db.Column('friend_id1', db.Integer, db.ForeignKey('users.id')),
	db.Column('friend_id2', db.Integer, db.ForeignKey('users.id')))

