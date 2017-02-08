# -*- coding: utf-8 -*-

__author__ = 'LIWEI240'

from wtforms import Form, BooleanField, TextField, PasswordField, StringField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired
from user import get_user_by_name

class LoginForm(FlaskForm):
    """Login Form"""

    username = StringField("username", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
    remember_me = BooleanField("Remember me", default=True)

    def validate(self):
        check_valid = super(LoginForm, self).validate()

        if not check_valid:
            return False


        # check user
        user = get_user_by_name(self.username.data)
        if not user:
            self.username.errors.append("Invalid username or password")
            return False

        # check password
        if not user.check_password(self.password.data):
            self.password.errors.append("Invalid password")
            return False
        return True