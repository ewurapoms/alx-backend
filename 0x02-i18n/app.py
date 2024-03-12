#!/usr/bin/env python3
"""Flask app"""

from flask import Flask, request, render_template, g
from flask_babel import Babel
import pytz
from datetime import datetime


class Config:
    """Configuration file"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> dict:
    """ creates user login system"""
    user_id = request.args.get('login_as')
    if user_id is not None and int(user_id) in users.keys():
        return users.get((int(user_id)))
    return None


@app.before_request
def before_request():
    """ display function"""
    g.user = get_user()


@babel.localeselector
def get_locale() -> str:
    """language selector"""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    if g.user and g.user['locale'] in app.config['LANGUAGES']:
        return g.user['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """Infer appropriate time zone"""
    timezone = request.args.get('timezone')
    if timezone:
        try:
            pytz.timezone(timezone)
            return timezone
        except pytz.UnknownTimeZoneError:
            pass
    if g.user:
        user_timezone = g.user.get("timezone")
        if user_timezone:
            try:
                pytz.timezone(user_timezone)
                return user_timezone
            except pytz.UnknownTimeZoneError:
                pass
    return app.config['BABEL_DEFAULT_TIMEZONE']


@app.route("/", strict_slashes=False)
def index() -> str:
    """route handler"""
    from datetime import datetime
    from flask_babel import format_datetime
    current_time = format_datetime(datetime.utcnow())
    return render_template("5-index.html", current_time=current_time)


if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0", debug=True)
