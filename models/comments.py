from flask import Flask, session, g
from db import db
from model_serializabler import Serializabler

class Comment(db.Model, Serializabler):
	__tablename__ = 'comments'
	id = db.Column(db.Integer, primary_key=True)
	body = db.Column(db.String(255), nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
	post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))