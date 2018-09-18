
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/',methods=['POST','GET'])
def index():
    return 'Hello from Flask!'