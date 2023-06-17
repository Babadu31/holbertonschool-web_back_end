#!/usr/bin/env python3
"""Module for Babel object instantiation"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)


class Config():
    """declaration of class Config"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def index():
    """Function renders 1-index"""
    return render_template('3-index.html')


@babel.localeselector
def get_locale():
    """Function matches best supported language"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == '__main__':
    app.run()
