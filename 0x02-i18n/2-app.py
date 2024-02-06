#!/usr/bin/env python3
'''Matching locale module'''

from flask import Flask, render_template, request
from flask_babel import Babel
from babel import negotiate_locale

app = Flask(__name__)
babel = Babel(app)


class Config:
    '''Config class'''
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    '''Matching languages'''
    return negotiate_locale(request.accept_languages, Config.LANGUAGES)


@app.route('/')
def index():
    '''index view functions'''
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(debug=True)
