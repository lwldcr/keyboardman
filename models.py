# -*- coding: utf-8 -*-
__author__ = 'LIWEI240'

"""
Models definition
"""


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