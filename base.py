# -*- coding: utf-8 -*-

from flask import Flask
from flask_login import LoginManager

app = Flask("KeyboardMan", static_folder="static")
app.secret_key = "No body knows"

lm = LoginManager()
lm.init_app(app)

# settings
lm.login_view = "login"
lm.session_protection = "strong"
lm.login_message = "Please login to access this page"
lm.login_message_category = "info"