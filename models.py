# -*- coding: utf-8 -*-
__author__ = 'LIWEI240'

"""
Models definition
"""

from hashlib import md5
from flask_login import UserMixin


class Post(object):
    __attrs__ = ["id", "title", "content", "pub_date", "author", "tags"]
    def __init__(self, data):
        for attr, val in zip(self.__attrs__, data):
            if attr == "id":
                val = int(val)
            if attr == "tags":
                val = val.split(",")
            setattr(self, attr, val)

    def __repr__(self):
        return "<Post: {}, title: {}, author: {}>".format(
            self.id,
            self.title,
            self.author
        )


class Author(object):
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

    def __repr__(self):
        return "<Author: {}, {}>".format(
            self.name,
            self.desc
        )


class User(UserMixin):
    """User class"""
    def __init__(self, username, password, id=-1, activated=True, permission=10):
        self.id = id
        self.username = username
        self.password = password
        self.activated = activated
        self.permission = permission

    @classmethod
    def get(cls, user_id):
        return User("user", "pass", 10)

    def is_authenticated(self):
        print('permi', self.permission)
        return self.permission <= 10

    def is_active(self):
        return self.activated

    def is_anonymouse(self):
        return False

    def get_id(self):
        return md5(str(self.id).encode('utf-8')).hexdigest()

    def check_password(self, passwd):
        print('given passwd:', passwd)
        if md5(str(passwd).encode('utf-8')).hexdigest() == self.password:
            return True
        return False

    def __repr__(self):
        return '<User: {}, activated: {}>'.format(
            self.username,
            self.activated
        )
