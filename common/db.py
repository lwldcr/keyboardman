# -*- coding: utf-8 -*-

__author__ = 'LIWEI240'

import sqlite3
from flask import g
from base import app
import os
from contextlib import closing

RootDir = os.path.dirname(__file__)
DataDir = os.path.join(RootDir, '..', 'data')
DB =  os.path.join(DataDir, 'posts.db')


def connect_db(db=DB):
    return sqlite3.connect(db)


def init_db():
    if not os.path.isdir(DataDir):
        try:
            os.mkdir(DataDir)
        except: # cannot make dir
            return

    with closing(connect_db()) as db:
        try:
            f = open('schema.sql', encoding='utf-8')
        except:
            f = open('schema.sql')

        db.cursor().executescript(f.read())
        db.commit()


class DbConn(object):
    def __init__(self, db=DB):
        self.db = db
        self.conn = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.db)
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            self.conn.commit()
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