# -*- coding: utf-8 -*-

__author__ = 'LIWEI240'

try:
    from urllib.parse import urlparse, urljoin
except:
    from urlparse import urljoin, urlparse

from flask import request


def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and \
        ref_url.netloc == test_url.netloc