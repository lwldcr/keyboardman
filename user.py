# -*- coding: utf-8 -*-

__author__ = 'LIWEI240'

"""
User related methods
"""

import os
from base import lm
from models import User
from common.db import DbConn

pwd = os.path.dirname(__file__)
DB = os.path.join(pwd, 'data', 'posts.db')

@lm.user_loader
def load_user(user_id):
    return User.get(user_id)


def get_user_by_name(username):
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


if __name__ == '__main__':
    print(get_user_by_name('bruce'))