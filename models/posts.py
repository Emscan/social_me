from flask import Flask
from db import db
from model_serializabler import Serializabler

class Post(db.Model, Serializabler):
	__tablename__ = 'posts'
	id = db.Column(db.Integer, primary_key=True)
	body = db.Column(db.String(1000), nullable=False)
	comments = db.relationship('Comment', backref='post', cascade='all, delete, delete-orphan')
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))