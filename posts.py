# -*- coding: utf-8 -*-

"""
Posts operations
"""

from common.db import DbConn
from models import Post

def list_all():
    """list all posts"""
    posts = []
    with DbConn() as db:
        cur = db.execute("select * from posts")
        posts_data = cur.fetchall()
    for data in posts_data:
        p = Post(data)
        posts.append(p)
    return posts


def get_post_by_id(pid):
    """get post by id"""
    post = None
    posts = get_post('id', pid)
    if len(posts) > 0:
        post = posts[0]
    return post


def get_posts_by_author(author):
    """get posts by author"""
    return get_post('author', author)


def get_posts_by_tag(tag):
    """get posts by tag"""
    return ["post1", "post2"]


def get_post(keytype, key):
    """general get post method"""
    posts = []
    sql = "select * from posts where {} = '{}'"
    if keytype and key:
        sql = sql % (keytype, key)
    else:
        return posts

    with DbConn() as db:
        cur = db.execute(sql)
        posts_data = cur.fetchall()

    for data in posts_data:
        p = Post(data)
        posts.append(p)
    return posts


def add_post(post):
    """add new post"""
    sql = "insert into `posts` (title, content, pub_date, author, tags) VALUES ('{}', '{}', '{}', '{}', '{}')"
    sql = sql.format(
        post.title,
        post.content,
        post.pub_date,
        post.author,
        ",".join(post.tags)
    )
    try:
        with DbConn() as db:
            db.execute(sql)
        return True
    except Exception as e:
        return False

def update_post(post):
    """update existing post"""
    sql = "update `posts` set title='{}',content='{}',pub_date='{}',author='{}',tags='{}' where id = {}"
    sql = sql.format(
        post.title,
        post.content,
        post.pub_date,
        post.author,
        ",".join(post.tags),
        post.id
    )
    try:
        with DbConn() as db:
            db.execute(sql)
        return True
    except Exception as e:
        return False


def delete_post(pid):
    """delete post matches given post id"""
    sql = "delete from `posts` where id = {}".format(pid)
    try:
        with DbConn() as db:
            db.execute(sql)
        return True
    except Exception as e:
        return False