#!/usr/bin/env python3
"""locale selector"""
from flask import Flask
from flask_babel import Babel
from requests import request


app = Flask(__name__)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """gets a locale"""
    return request.accept_languages.best_match(['en', 'es'])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
