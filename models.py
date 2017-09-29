# -*- coding: utf-8 -*-
__author__ = 'LIWEI240'

"""
Models definition
"""

import os
from hashlib import md5
from common.db import DbConn

pwd = os.path.dirname(__file__)
DB = os.path.join(pwd, 'data', 'posts.db')


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

    def tags_valid(self):
        if not self.tags:
            return False
        if type(self.tags) != list:
            return False
        if len(''.join(self.tags)) <= 0:
            return False
        return True

class Author(object):
    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

    def __repr__(self):
        return "<Author: {}, {}>".format(
            self.name,
            self.desc
        )


class User(object):
    """User class"""
    def __init__(self, username, password, id=-1, activated=True, permission=10):
        self.id = id
        self.username = username
        self.password = password
        self.activated = activated
        self.permission = permission


    @classmethod
    def get_user_by_name(cls, username):
        """Get user by given username"""
        sql = "select * from `users` where username = '{}'".format(username)

        try:
            with DbConn(DB) as conn:
                cur = conn.execute(sql)
                data = cur.fetchone()
            if data:
                user = User(data[1], data[2], data[0], data[3], data[4])
            else:
                user = None
        except Exception as e:
            user = None
        return user

    @classmethod
    def verify(cls, username, password, user_obj):
        try:
            user_obj = User.get_user_by_name(username)
#            print(user, password, user_obj.username, user_obj.password)
            if md5(str(password).encode('utf-8')).hexdigest() == user_obj.password:
                return True
        except Exception as e:
            print(e)
            return False

    def __repr__(self):
        return '<User: {}, activated: {}>'.format(
            self.username,
            self.password
        )


def add_user(username, password):
    try:
        if User.get_user_by_name(username):
            return False
        user = User(username, password)
        sql = "insert into `users` (username,password,activated,permission_level) values ('{}','{}',{},{})".format(
                user.username,
                md5(str(user.password).encode('utf-8')).hexdigest(),
                1 if user.activated else 0,
                user.permission
        )
        with DbConn(DB) as db:
            db.execute(sql)
    except Exception as e:
        print(e)
        return False
    return True

if __name__ == '__main__':
    u = User.get_user_by_name("bruce")
    print(u)