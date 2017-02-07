# -*- coding: utf-8 -*-

__author__ = 'LIWEI240'

"""
Todo app models definition
"""

import datetime
from enum import Enum

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


class Todo(object):
    """Todo class

        define a todo class
    """
    def __init__(self, title, desc='', start='', end='', level=3, status=Status.not_started.name, id=-1):
        self.id = id
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