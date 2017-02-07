# -*- coding: utf-8 -*-

__author__ = 'LIWEI240'

from . import api

# TODO: implement apis


@api.route("/list")
def list_posts():
    """Return all posts list"""
    return "Test OK"
