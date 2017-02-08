# -*- coding: utf-8 -*-

__author__ = 'LIWEI240'

"""
Admin views
"""

from flask_admin import BaseView, expose
from flask_login import current_user

class MyView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin.html')

    def is_accessible(self):
        return current_user.is_authenticated()