# -*- coding: utf-8 -*-

__author__ = 'LIWEI240'

from flask import Blueprint

todo = Blueprint('todo', __name__)

from . import views