# -*- coding: utf-8 -*-

from base import app
from flask import render_template, flash, request, abort, redirect,\
    url_for, session, jsonify
import posts
from utils import is_safe_url
from models import User, add_user, Post
from posts import add_post
import re
import datetime

html_filter = re.compile(r'\<.*?\>')

@app.route("/")
def index():
    all_posts = posts.list_all()
    # TODO: render template with posts
    return render_template("index.html", posts=all_posts)


@app.route("/login", methods=["GET", "POST"])
def login():
    errmsg = ""
    if request.method == 'POST':
        username = request.form.get('username', '')
        password = request.form.get('password', '')
        user_obj = User.get_user_by_name(username)
        if not User.verify(username, password, user_obj):
            errmsg="Login failed"

        if not errmsg:
            flash('Logged in successfully')
            session['username'] = username
            session['permission'] = user_obj.permission
            _next = request.args.get('next')

            if not is_safe_url(_next):
                return abort(400)
            return redirect(_next or url_for('index'))
    return render_template("login.html", errmsg=errmsg)


@app.route("/post/<int:pid>")
def post_detail(pid):
    post = posts.get_post_by_id(pid)
    return render_template("post.html", post=post)


@app.route("/post/create", methods=["GET", "POST"])
def post_create():
    if request.method == 'GET':
        return render_template("post_create.html")
    else:
        title = request.form.get('title')
        text = request.form.get('editor1')
        tags = html_filter.findall(text)
        for tag in tags:
            text = text.replace(tag, '')

        p = Post([-1, title.encode('utf-8'), text.encode('utf-8'),
                  datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), session.get('username'), ''])

        ret = add_post(p)
        if ret:
            return redirect(url_for('index'))
        else:
            return redirect(url_for('post_create'))


@app.route("/post/<int:pid>/edit", methods=["GET", "POST"])
def post_edit(pid):
    post = posts.get_post_by_id(pid)
    post.content = post.content.replace('\r\n', '<br>\r\n')
    if request.method == 'GET':
          return render_template("post_edit.html", post=post)
    else:
        raw_content = request.form.get('editor1')
        tags = html_filter.findall(raw_content)
        for tag in tags:
            raw_content = raw_content.replace(tag, '')
        post.content = raw_content.encode('utf-8')
        posts.update_post(post)
        return redirect(url_for('index'))


@app.route("/post/<int:pid>/delete", methods=["GET", "POST"])
def post_delete(pid):
    ret = posts.delete_post(pid)
    return jsonify({'status': ret})


@app.route("/logout")
def logout():
    session.pop('username')
    session['permission'] = 20
    return redirect(url_for('index'))


@app.route("/register", methods=['GET', 'POST'])
def register():
    if  request.method == "GET":
        return render_template("register.html")
    elif request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(username, password)
        ret = add_user(username, password)
        if ret:
            return redirect(url_for("login"))
        else:
            return redirect(url_for("register"))