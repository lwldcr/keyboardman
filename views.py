# -*- coding: utf-8 -*-

from base import app
from flask import render_template, flash, request, abort, redirect, url_for
import posts
from forms import LoginForm
from utils import is_safe_url
from user import get_user_by_name
from flask_login import login_user, logout_user, login_required, current_user


@app.route("/")
def index():
    print(current_user)
    all_posts = posts.list_all()
    # TODO: render template with posts
    return render_template("index.html", posts=all_posts)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = get_user_by_name(form.username.data)
        login_user(user)
        flash('Logged in successfully')
        _next = request.args.get('next')

        if not is_safe_url(_next):
            return abort(400)
        return redirect(_next or url_for('index'))
    return render_template("login.html", title="登陆", form=form)


@app.route("/logout")
@login_required
def logout():
    print("logout")
    logout_user()
    return redirect(url_for('index'))