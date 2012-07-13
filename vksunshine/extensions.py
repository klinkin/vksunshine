#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask.ext.seasurf import SeaSurf
from flask.ext.oauth import OAuth
from vksunshine.config import VK_BASE_URL, VK_ACCESS_TOKEN_URL, VK_AUTHORIZE_URL, \
                              VK_REQUEST_TOKEN_PARAMS, VK_CONSUMER_KEY, VK_CONSUMER_SECRET


__all__ = ['csrf', 'oauth_manager', 'vkontakte']

csrf = SeaSurf()
oauth_manager = OAuth()


vkontakte = oauth_manager.remote_app('vkontakte',
    base_url=VK_BASE_URL,
    authorize_url=VK_AUTHORIZE_URL,
    request_token_url=None,
    request_token_params=VK_REQUEST_TOKEN_PARAMS,
    access_token_url=VK_ACCESS_TOKEN_URL,
    consumer_key=VK_CONSUMER_KEY,
    consumer_secret=VK_CONSUMER_SECRET)
