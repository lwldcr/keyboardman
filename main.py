# -*- coding: utf-8 -*-

import views
from base import app
from todo import todo
from api_v1 import api

app.register_blueprint(todo, url_prefix="/todo")
app.register_blueprint(api, url_prefix="/api/v1")

if __name__ == '__main__':
    app.run(debug=True)