#!/usr/bin/env python3
"""flask app"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def index():
    """index router"""
    return render_template('0-index.html')
