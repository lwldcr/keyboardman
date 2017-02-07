# -*- coding: utf-8 -*-

__author__ = 'LIWEI240'

from flask import Blueprint

api = Blueprint('api', __name__)

from . import views