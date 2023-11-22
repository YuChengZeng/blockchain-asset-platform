# -*- coding: utf-8 -*-
from sqlalchemy import Column, Integer, BigInteger, String, Boolean, ForeignKey, DateTime, Boolean, Text, LargeBinary
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()


class Asset_nft(Base):
	__tablename__ = 'asset_nft'
	NftId = Column(Integer, primary_key=True)
	sha = Column(String(256))
	time = Column(Integer)
	operator = Column(String(42))
	transactionHash = Column(String(128))
	blockNumber = Column(Integer)
	source = Column(String(128))


class Asset_detail(Base):
	__tablename__ = 'asset_detail'
	id = Column(Integer, primary_key=True)
	title = Column(String(64))
	creator = Column(String(64))
	description = Column(String)
	subject = Column(String(64))
	format = Column(String(10))
	transactionHash = Column(String(128))


class Launch_to_nft(Base):
	__tablename__ = 'launch_to_nft'
	launch_id = Column(Integer, primary_key=True)
	tokenId = Column(Integer)
	operator = Column(String(42))
	status = Column(Integer)
	price = Column(Integer)
	blockNumber = Column(Integer)


class Pi_user(Base):
	__tablename__ = 'pi_user'
	id = Column(Integer, primary_key=True)
	nickname = Column(String(256))
	account = Column(String(256))
	password = Column(String(256))
	token = Column(String(512))
	_id = Column(String(128))
	email = Column(String(128))
	address = Column(String(42))


class Set_room(Base):
	__tablename__ = 'set_room'
	id = Column(Integer, primary_key=True)
	address = Column(String(42))
	room_id = Column(String(64))
	price = Column(Integer)
	blockNumber = Column(Integer)


class Ticket(Base):
	__tablename__ = 'ticket'
	id = Column(Integer, primary_key=True)
	address = Column(String(42))
	ticket_id = Column(Integer)
	room_id = Column(String(64))
	price = Column(Integer)
	blockNumber = Column(Integer)


class Room_list(Base):
	__tablename__ = 'room_list'
	id = Column(Integer, primary_key=True)
	room_id = Column(String(64))
	coverUrl = Column(String(128))
	signboardUrl = Column(String(128))
	title = Column(String(64))
	introduction = Column(String(2048))


class Interact(Base):
	# 點讚
	__tablename__ = 'interact'
	id = Column(Integer, primary_key=True)
	address = Column(String(42))
	room_id = Column(String(64))
	target = Column(String(128))
	interact = Column(String(32))
	status = Column(Integer)


class Application_list(Base):
	__tablename__ = 'application_list'
	id = Column(Integer, primary_key=True)
	operator = Column(String(42))
	licenseId = Column(Integer)
	launchId = Column(Integer)
	price = Column(Integer)
	blockNumber = Column(Integer)