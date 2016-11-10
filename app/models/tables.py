from sqlalchemy import Column, String, Integer
from app import Base

class User(Base):
	__tablename__ = 'users'
	id = Column(Integer, primary_key=True)
	username = Column(String(30), unique=True, nullable=False)
	password = Column(String(30), nullable=False)

	def __init__(self, username, password):
		self.username = username
		self.password = password

	def __repr__(self):
		return '<User: %s>' % self.username
