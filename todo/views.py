# -*- coding: utf-8 -*-

__author__ = 'LIWEI240'

"""
todo views
"""

from . import todo
import todo.todo_ops as ops
from todo.model import Todo
from flask import request, jsonify
from common.const import Const


@todo.route("/list")
def list_todo():
    """List all todo objects"""
    ret = ops.list_all()
    return jsonify(ret)


@todo.route("/add", methods=["POST"])
def add_todo():
    ret = {'status': 0, 'msg': 'OK'}
    form = request.form
    title = form.get('title', '')
    if not title:
        ret['status'] = Const.RetCode.InvalidParam
        ret['msg'] = 'title must not leave blank!'
    else:
        desc = form.get('desc', '')
        start = form.get('start', '')
        end = form.get('end', '')
        level = int(form.get('level', 3))
        todo = Todo(title, desc, start, end, level)
        ret = ops.add_new_todo(todo, ret)
    return jsonify(ret)


@todo.route("/done/<todo_id>")
def done_todo(todo_id):
    ret = {'status': 0, 'msg': 'OK'}
    if not str(todo_id).isdigit():
        ret['status'] = Const.RetCode.InvalidParam
        ret['msg'] = "todo_id should be a number"

    todo = ops.get_todo(todo_id)
    if todo:
        todo.done()
        ret = ops.update_todo(todo, ret)
    else:
        ret['status'] = Const.RetCode.NotExist
        ret['msg'] = "no todo match id: {}".format(todo_id)

    return jsonify(ret)


@todo.route("/delete/<todo_id>")
def delete_todo(todo_id):
    ret = {'status': 0, 'msg': 'OK'}
    if not str(todo_id).isdigit():
        ret['status'] = Const.RetCode.InvalidParam
        ret['msg'] = "todo_id should be a number"

    else:
        ret = ops.delete_todo(todo_id, ret)
    return jsonify(ret)