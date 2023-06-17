#!/usr/bin/env python3
"""Route module for the API"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Dict


app = Flask(__name__)
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """Config class"""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """Get locale"""
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    if hasattr(g, 'user') and g.user and \
            g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']
    header_locale = request.accept_languages.best_match(
        app.config['LANGUAGES'])
    if header_locale:
        return header_locale
    return app.config['BABEL_DEFAULT_LOCALE']

@babel.localeselector
def get_locale():
    """Retrieves locale from request"""
    locale = request.args.get('locale')
    if locale and locale in Config.LANGUAGES:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])

def get_user():
    """Returns a user dictionary or None if the ID cannot be found"""
    user_id = request.args.get('login_as')
    if user_id:
        user = users.get(int(user_id))
        return user
    return None


@app.before_request
def before_request():
    """Find a user if any, and set it as a global on flask.g.user"""
    g.user = get_user()


@app.route('/')
def home():
    """Home route"""
    return render_template('5-index.html')


if __name__ == '__main__':
    app.config['LANGUAGES'] = ['en', 'fr']
    app.config['BABEL_DEFAULT_LOCALE'] = 'en'
    app.run()
