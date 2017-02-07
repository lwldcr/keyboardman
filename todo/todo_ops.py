# -*- coding: utf-8 -*-

__author__ = 'LIWEI240'

"""
Todo objects persistent and management
"""

import os
import json
from common.db import DbConn
from common.const import Const
from todo.model import Todo

pwd = os.path.dirname(__file__)
DB = os.path.join(pwd, '..', 'data', 'todo.db')


def init_todo():
    """Init todo db"""
    with DbConn(DB) as db:
        with open('todo_schema.sql', encoding='utf-8') as f:
            db.cursor().executescript(f.read())
        db.commit()
    print("todo db init done!")


def add_new_todo(todo, ret):
    """Save todo object to file"""
    sql = "insert into `todo` (title, desc, start, end, level, status) values " + \
          "('{}', '{}', '{}', '{}', {}, '{}')".format(
              todo.title, todo.desc,
              todo.start, todo.end,
              todo.level, todo.status
          )
    with DbConn(DB) as db:
        try:
            db.execute(sql)
            ret['msg'] = "OK"
        except Exception as e:
            ret['status'] = Const.RetCode.ParseError
            ret['msg'] = "add new todo failed: {}".format(e)
    return ret


def list_all():
    """Return all todo list"""
    ret = {'status': 0, 'msg': '', 'todos': None}
    todos = []
    sql = "select * from todo"
    raw_data = None
    with DbConn(DB) as db:
        try:
            cur = db.execute(sql)
            raw_data = cur.fetchall()
        except Exception as e:
            ret['status'] = Const.RetCode.ParseError
            ret['msg'] = "get all todo failed: {}".format(e)
    if raw_data:
        keys = ['id', 'title', 'desc', 'start', 'end', 'level', 'status']
        for d in raw_data:
            todo = Todo(**dict(zip(keys, d)))
            todos.append(todo.__dict__)
    ret['todos'] = todos
    return ret


def get_todo(todo_id):
    """Return todo with given todo_id"""
    sql = "select * from todo where id = {}".format(todo_id)
    with DbConn(DB) as db:
        try:
            cur = db.execute(sql)
            raw_data = cur.fetchone()
        except Exception as e:
            raw_data = []

    todo = None
    if raw_data:
        keys = ['id', 'title', 'desc', 'start', 'end', 'level', 'status']
        todo = Todo(**dict(zip(keys, raw_data)))
    return todo


def update_todo(todo, ret):
    sql = "update todo set title='{}',desc='{}',start='{}',end='{}',level={},status='{}' \
          where id = {}".format(
                todo.title, todo.desc,
                todo.start, todo.end,
                todo.level, todo.status,
                todo.id
            )
    with DbConn(DB) as db:
        try:
            db.execute(sql)
        except Exception as e:
            ret['status'] = Const.RetCode.ParseError
            ret['msg'] = "update todo: {} failed: {}".format(todo.id, e)
    return ret


def delete_todo(todo_id, ret):
    """Delete todo matches given todo_id"""
    todo = get_todo(todo_id)
    if not todo:
        ret['status'] = Const.RetCode.NotExist
        ret['msg'] = "todo item not exist: {}".format(todo_id)
        return ret

    sql = "delete from todo where id = {}".format(todo_id)
    with DbConn(DB) as db:
        try:
            db.execute(sql)
        except Exception as e:
            ret['status'] = Const.RetCode.ParseError
            ret['msg'] = "delete todo: {} failed: {}".format(todo_id, str(e))
    return ret

if __name__ == '__main__':
    init_todo()
    print(list_all())