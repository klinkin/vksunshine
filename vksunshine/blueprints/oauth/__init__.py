#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
from flask import Blueprint, request, redirect, url_for, session, flash, g
from vksunshine.extensions import vkontakte
from vksunshine.models import User

bp = Blueprint('oauth', __name__, template_folder='templates')

@vkontakte.tokengetter
def get_vkontakte_token():
    """This is used by the API to look for the auth token and secret
    it should use for API calls.  During the authorization handshake
    a temporary set of token and secret is used, but afterwards this
    function has to return the token and secret.  If you don't want
    to store this in the database, consider putting it into the
    session instead.
    """
    user = g.user
    if user is not None:
        return user.access_token, ''

@bp.route('/login')
def login():
    redirect_uri = url_for('oauth.oauth_authorized', _external = True, next=request.args.get('next') or request.referrer or None)
    return vkontakte.authorize(callback=redirect_uri)

@bp.route('/logout')
def logout():
    session.pop('user_id', None)
    flash('You were signed out')
    return redirect(request.referrer or url_for('frontend.promo'))


@bp.route('/oauth-authorized')
@vkontakte.authorized_handler
def oauth_authorized(resp):
    """Called after authorization.  After this function finished handling,
    the OAuth information is removed from the session again.  When this
    happened, the tokengetter from above is used to retrieve the oauth
    token and secret.

    Because the remote application could have re-authorized the application
    it is necessary to update the values in the database.

    If the application redirected back after denying, the response passed
    to the function will be `None`.  Otherwise a dictionary with the values
    the application submitted.  Note that vkontakte itself does not really
    redirect back unless the user clicks on the application name.
    """
    next_url = request.args.get('next') or url_for('frontend.promo')
    if resp is None:
        flash(u'You denied the request to sign in.')
        return redirect(next_url)

    user = User.get_by_id(resp['user_id'])

    # user never signed on
    if user is None:
        user = User(id=resp['user_id'], user_id=resp['user_id'], access_token=resp['access_token'], expires_in=resp['expires_in'])
        user.put()

    session['user_id'] = user.user_id
    flash('You were signed in')
    return redirect(next_url)
