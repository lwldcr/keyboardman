# -*- coding: utf-8 -*-

import views
from base import app
from todo import todo
app.register_blueprint(todo, url_prefix="/todo")

if __name__ == '__main__':
    app.run(debug=True)