from turtle import title
from . import main
from flask import render_template,Flask


@main.route('/')
def index():
    title = 'Blog'

    return render_template('index.html',title=title)