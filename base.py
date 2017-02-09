# -*- coding: utf-8 -*-

from flask import Flask

app = Flask("KeyboardMan", static_folder="static")
app.secret_key = "No body knows"