# -*- coding: utf-8 -*-
from __future__ import absolute_import

import logging
from flask import current_app, url_for, redirect, render_template, abort, request, session, flash, g
from flask.views import View
from flask.ext.babel import refresh, gettext, lazy_gettext as _

from vksunshine.extensions import vkontakte

class Home(View):

    def __init__(self, template_name):
        self.template_name = template_name
        self.title = _('Userena Promo')

    def render_template(self, context):
        return render_template(self.template_name, **context)

    def dispatch_request(self):
        vk_user_info = None
        vk_user_wall = None

        if g.user is not None:
            data = {
                     'uids':g.user.user_id, 
                     'fields': 'uid,first_name,last_name,nickname,screen_name,sex,bdate,city,country,timezone,photo,photo_medium,photo_big,has_mobile,rate,contacts,education,online,counters',
                     'access_token':g.user.access_token,
                   }

            resp = vkontakte.get('users.get', data)
            if resp.status == 200:
                vk_user_info = resp.data
            else:
                flash('Unable to load userinfo from vkontakte. Maybe out of '
                      'API calls or vkontakte is overloaded.')					
            data = {
                     'owner_id':g.user.user_id, 
                     'offset': 0,
                     'count':10,
                   }

            resp = vkontakte.get('wall.get', data)
            if resp.status == 200:
                vk_user_wall = resp.data
            else:
                flash('Unable to load userinfo from vkontakte. Maybe out of '
                      'API calls or vkontakte is overloaded.')

        context = {'user_info': vk_user_info, 'user_wall': vk_user_wall}
        return self.render_template(context)