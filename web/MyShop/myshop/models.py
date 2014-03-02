from datetime import datetime
from sqlalchemy import (
	Column,
	ForeignKey,
	Integer,
	Text,
	Unicode,
	)

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
	scoped_session,
	sessionmaker,
	relationship
	)

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()


class User(Base):
	__tablename__ = 'users'

	id = Column(Integer, primary_key=True)
	name = Column(Unicode(255), nullable=False)
	password = Column(Unicode(255), nullable=False)
	email = Column(Unicode(255))
	
	group_id = Column(Integer, ForeignKey('groups.id'), nullable=False)
	group = relationship('Group', backref='users')


class Group(Base):
	__tablename__ = 'groups'

	id = Column(Integer, primary_key=True)
	name = Column(Unicode(255), nullable=False)


class Permission(Base):
	__tablename__ = 'permissions'

	id = Column(Integer, primary_key=True)
	name = Column(Unicode(255), nullable=False)


class Item(Base):
	__tablename__ = 'items'

	id = Column(Integer, primary_key=True)
	name = Column(Unicode(255), nullable=False)
	description = Column(Text)
	price = Column(Float, nullable=False, default=0.0)

	category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)
	category = relationship('Category', backref='items')


class Category(Base):
	__tablename__ = 'categories'

	id = Column(Integer, primary_key=True)
	name = Column(Unicode(255), nullable=False)
	parent_id = Column(Integer, ForeignKey('categories.id'), nullable=True)
	parent = relationship('Category', backref='children')


class ItemImage(Base):
	__tablename__ = 'images'

	id = Column(Integer, primary_key=True)
	path = Column(Unicode(255), nullable=False)
	item_id = Column(Integer, ForeignKey('items.id'), nullable=False)
	item = relationship('Item', backref='images')


class Comment(Base):
	__tablename__ = 'comments'

	id = Column(Integer, primary_key=True)
	user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
	user = relationship('User', backref='comments')
	item_id = Column(Item, ForeignKey('items.id'), nullable=False)
	item = relationship('Item', backref='comments')

	rank = Column(Integer, nullable=False, default=3);
	content = Column(Text)


class Cart(Base):
	__tablename__ = 'carts'

	id = Column(Integer, primary_key=True)

	# TODO: Many-to-many
	items = relationship('Item')
	user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
	user = relationship('User', backref='cart')


class Order(Base):
	__tablename__ = 'orders'

	id = Column(Integer, primary_key)
	user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
	user = relationship('User', 'orders')

	# TODO: Many-to-many
	items = relationship('Item')
	add_time = Column(DateTime, nullable=False, default=datetime.now())

	address = Column(Unicode(255), nullable=False)
	telephone = Column(Unicode(25), nullable=False)
