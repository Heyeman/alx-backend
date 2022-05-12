#!/usr/bin/env python3
""" sth unknown"""
from flask import Flask, render_template
from flask_babel import Babel


class Config():
    """config class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"



app = Flask(__name__)
app.config.from_object(1-app.config)
babel = Babel(app)


@app.route('/')
def hello():
    """func"""
    return render_template('1-index.html')
