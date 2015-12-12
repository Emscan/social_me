from flask import Flask
from db import db
from model_serializabler import Serializabler

friendships = db.Table('friendships', 
	db.Column('friend_id1', db.Integer, db.ForeignKey('users.id')),
	db.Column('friend_id2', db.Integer, db.ForeignKey('users.id')))

class FriendshipRequest(db.Model, Serializabler):
	__tablename__ = 'friendship_requests'
	id = db.Column(db.Integer, primary_key=True)
	requesting_id = db.Column(db.Integer, db.ForeignKey('users.id'))
	requested_id = db.Column(db.Integer, db.ForeignKey('users.id'))

	def delete_friend(self, friend):
		try:
			db.session.delete(self)
			db.session.commit()
		except:
			db.session.rollback

	def accept_friend(self, friend):
		self.sender.make_friend(self.receiver)
		self.delete()

	@classmethod
	def send_request(cls, user_id, friend_id):
		friend_request = FriendshipRequest(requesting_id=user_id, requested_id=friend_id)
		db.session.add(friend_request)
		db.session.commit()

	@classmethod
	def from_id(cls, request_id):
		return cls.query.filter(cls.id == request_id).first()

