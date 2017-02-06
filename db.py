# -*- coding: utf-8 -*-

__author__ = 'LIWEI240'

import sqlite3
from flask import g
from base import app
import os
from contextlib import closing

RootDir = os.path.dirname(__file__)
DB = os.path.join(RootDir, 'data', 'posts.db')


def connect_db():
    return sqlite3.connect(DB)


def init_db():
    with closing(connect_db()) as db:
        with open('schema.sql', encoding='utf-8') as f:
            db.cursor().executescript(f.read())
        db.commit()


class DbConn(object):
    def __init__(self):
        self.db = DB
        self.conn = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.db)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            self.conn.close()
        except Exception as e:
            print(e)


@app.before_request
def before_request():
    g.db = connect_db()
    print("db connected")


@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()
    print("db closed")


if __name__ == '__main__':
    init_db()