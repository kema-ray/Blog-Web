from . import main
from flask import render_template,Flask
from ..requests import get_quote
from flask_login import login_required


@main.route('/')
def index():
    title = 'Blog'

    random_quote = get_quote()

    return render_template('index.html',title=title,quote=random_quote)