#!/usr/bin/env python3
"""basic flask app"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/index.html')
def index():
    return render_template('index.html')    