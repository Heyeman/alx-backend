#!/usr/bin/env python3
""" sth unknown"""
from flask import Flask, render_template
from flask_babel import Babel


class Config():
    """config class"""
    LANGUAGES = ["en", "fr"]


app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = Config.LANGUAGES[1]
app.config['BABEL_DEFAULT_TIMEZONE'] = "UTC"
babel = Babel(app)


@app.route('/')
def hello():
    """func"""
    return render_template('1-index.html')
