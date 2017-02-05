# -*- coding: utf-8 -*-

"""
Posts operations
"""


def list_all():
    """list all posts"""
    # TODO
    return ["post1", "post2"]


def get_post_by_id(pid):
    """get post by id"""
    return "post"


def get_posts_by_author(author):
    """get posts by author"""
    return ["post1", "post2"]


def get_posts_by_tag(tag):
    """get posts by tag"""
    return ["post1", "post2"]


def get_post(keytype, key):
    """general get post method"""
    sql = "select * from posts where %s = '%s'"
    if keytype and key:
        sql = sql % (keytype, key)
    else:
        return None

    try:
        # TODO: read db
        print(sql)
    except Exception as e:
        print(e)
    return "post"


def add_post(post):
    """add new post"""
    # TODO
    return True


def update_post(post):
    """update existing post"""
    # TODO
    return True


def delete_post(pid):
    """delete post matches given post id"""
    # TODO
    return True