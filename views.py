# -*- coding: utf-8 -*-

from base import app
from flask import render_template
import posts

@app.route("/")
def index():
    all_posts = posts.list_all()
    # TODO: render template with posts
    return render_template("index.html", posts=all_posts)

@app.route("/login", methods=["GET", "POST"])
def login():
    # TODO
    return "logged in"


@app.route("/logout")
def logout():
    # TODO
    return "logged out"

@app.route("/admin")
def admin():
    # TODO
    return "admin page"