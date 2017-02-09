# -*- coding: utf-8 -*-

__author__ = 'LIWEI240'

"""
Todo app models definition
"""

import os
import datetime
from enum import Enum
from common.db import DbConn

pwd = os.path.dirname(__file__)
DB = os.path.join(pwd, '..', 'data', 'todo.db')

TIME_FMT = "%Y-%m-%d %H:%M:%S"

class StatusException(Exception):
    pass


class Status(Enum):
    """Todo status enum"""
    not_started = 1
    working = 2
    dropped = 3
    done = 4
    overdue = 5


class Category(object):
    """Todo Category"""
    def __init__(self, name, extra=''):
        self.name = name
        self.extra = extra

    def __repr__(self):
        return '<Category: {}>'.format(
            self.name
        )

    @classmethod
    def get(cls, category_id):
        sql = "select * from category where id = {}".format(category_id)
        with DbConn(DB) as db:
            try:
                cur = db.execute(sql)
                raw_data = cur.fetchone()
            except Exception as e:
                raw_data = []

        category = None
        if raw_data:
            keys = ['name', 'extra']
            category = Category(**dict(zip(keys, raw_data[1:])))
            category.id = raw_data[0]
        return category


class Todo(object):
    """Todo class

        define a todo class
    """
    def __init__(self, title, desc='', start='', end='', level=3, status=Status.not_started.name, id=-1, category_id=1):
        self.id = id
        self.category_id = category_id
        self.title = title
        self.desc = desc
        if not start:
            start = datetime.datetime.now().strftime(TIME_FMT)
        if not end:
            end = datetime.datetime.now() + datetime.timedelta(days=7)
            end = end.strftime(TIME_FMT)
        self.start = start
        self.end = end
        self.level = level
        self.status = status

    def update_status(self, status):
        if status not in Status:
            raise StatusException("Wrong status: {}".format(status))

        self.status = Status.get(status).name

    def done(self):
        self.status = Status.done.name

    def change_category(self, category_id):
        """change todo's category"""
        new_category = Category.get(category_id)
        if not new_category:
            return False
        else:
            self.category_id = category_id
            return True

    def __repr__(self):
        return '<Todo: {}, status: {}, ends: {}>'.format(
            self.title,
            self.status,
            self.end
        )

if __name__ == '__main__':
    s = Status['not_started']
    print(s.name)
    print(s.value)