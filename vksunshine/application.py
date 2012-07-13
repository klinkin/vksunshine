#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging

from flask import Flask, g, redirect, render_template, request, session, jsonify, url_for, make_response

from vksunshine.blueprints import frontend, oauth
from vksunshine.models import User

__all__ = ["create_app"]

DEFAULT_APP_NAME = "vksunshine"

DEFAULT_BLUEPRINTS = (
     (frontend.bp, '/'),
     (oauth.bp, '/oauth'),
)

def create_app(config=None, app_name=None, blueprints=None):

    if app_name is None:
        app_name = DEFAULT_APP_NAME

    if blueprints is None:
        blueprints = DEFAULT_BLUEPRINTS

    app = Flask(__name__)
    configure_app(app)

    configure_errorhandlers(app)

    configure_before_handlers(app)

    configure_extensions(app)

    configure_jinja(app)
    configure_context_processors(app)

    configure_blueprints(app, blueprints)

    logging.info(repr(app.url_map))

    return app

def configure_app(app):
    app.config.from_object('vksunshine.config')

def configure_blueprints(app, blueprints):
    for blueprint, url_prefix in blueprints:
        app.register_blueprint(blueprint, url_prefix=url_prefix)

def configure_before_handlers(app):
    @app.before_request
    def before_request():
        g.user = None
        if 'user_id' in session:
            g.user = User.get_by_id(session['user_id'])

def configure_extensions(app):
    pass


def configure_context_processors(app):

    @app.context_processor
    def config():
        return dict(config=app.config)

def format_exception(tb):
    res = make_response(tb.render_as_text())
    res.content_type = 'text/plain'
    return res

def configure_jinja(app):
    # http://flask.pocoo.org/snippets/74/
    app.jinja_env.exception_formatter = format_exception
		
def configure_errorhandlers(app):
    @app.errorhandler(404)
    def page_not_found(error):
        if request.is_xhr:
            return jsonify(error=('Sorry, page not found'))
        return render_template("errors/404.html", error=error)

    @app.errorhandler(403)
    def forbidden(error):
        if request.is_xhr:
            return jsonify(error=('Sorry, not allowed'))
        return render_template("errors/403.html", error=error)

    @app.errorhandler(500)
    def server_error(error):
        if request.is_xhr:
            return jsonify(error=('Sorry, an error has occurred'))
        return render_template("errors/500.html", error=error)

    @app.errorhandler(401)
    def unauthorized(error):
        if request.is_xhr:
            return jsonify(error=("Login required"))
#        flash(userena_manager.login_manager.login_message, "error")
#        return redirect(url_for(userena_manager.login_manager.login_view))
        return redirect(url_for(frontend.promo))