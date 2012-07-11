# -*- coding: utf-8 -*-
from __future__ import absolute_import

import logging
from flask import current_app, url_for, redirect, render_template, abort, request, session, flash, g, jsonify
from flask.views import View
from flask.ext.babel import refresh, gettext, lazy_gettext as _

from vksunshine.extensions import vkontakte

class Home(View):

    def __init__(self, template_name):
        self.template_name = template_name
        self.title = _('VkSunshine Promo')

    def render_template(self, context):
        return render_template(self.template_name, **context)

    def dispatch_request(self):
        vk_user_info = None
        vk_user_news = None

        if g.user is not None:
            data = {
                     'uids':g.user.user_id, 
                     'fields': 'uid,first_name,last_name,nickname,screen_name, activity, sex,bdate,city,country,timezone,photo,photo_medium,photo_big,has_mobile,rate,contacts,education,online,counters',
                     'access_token':g.user.access_token,
                   }


            resp = vkontakte.get('users.get', data)
            if resp.status == 200:
                vk_user_info = resp.data['response'][0]
            else:
                flash('Unable to load userinfo from vkontakte. Maybe out of '
                      'API calls or vkontakte is overloaded.')					
            data = {
                     'owner_id':g.user.user_id, 
                     'offset': 0,
                     'filter':'all',
                     'count':100,
                   }

            resp = vkontakte.get('wall.get', data)
            if resp.status == 200:
                vk_user_news = resp.data['response']
            else:
                flash('Unable to load userinfo from vkontakte. Maybe out of '
                      'API calls or vkontakte is overloaded.')

        context = {'user_info': vk_user_info, 'user_news': vk_user_news}
        return self.render_template(context)

class News(View):

    def __init__(self, template_name):
        self.template_name = template_name
        self.title = _('User\'s news')

    def render_template(self, context):
        return render_template(self.template_name, **context)

    def dispatch_request(self):
        vk_user_info = None
        vk_user_news = None

        if g.user is not None:
            data = {
                     'uids':g.user.user_id, 
                     'fields': 'uid,first_name,last_name,nickname,screen_name, activity, sex,bdate,city,country,timezone,photo,photo_medium,photo_big,has_mobile,rate,contacts,education,online,counters',
                     'access_token':g.user.access_token,
                   }


            resp = vkontakte.get('users.get', data)
            if resp.status == 200:
                vk_user_info = resp.data['response'][0]
            else:
                flash('Unable to load userinfo from vkontakte. Maybe out of '
                      'API calls or vkontakte is overloaded.')					
	
            data = {
                     'owner_id':g.user.user_id, 
                     'offset': 0,
                     'filter':'all',
                     'count':100,
                   }

            resp = vkontakte.get('wall.get', data)
            if resp.status == 200:
                vk_user_news = resp.data['response']
            else:
                flash('Unable to load userinfo from vkontakte. Maybe out of '
                      'API calls or vkontakte is overloaded.')

        context = {'user_info':vk_user_info, 'user_news': vk_user_news}
        return self.render_template(context)

class AddNews(View):
    methods = ['GET', 'POST']
    def dispatch_request(self):
        result = None
        if g.user is not None:
            message = request.values.get('message')
            logging.info("request.values.get('message') = " + str(request.values.get('message')))

            data = {'owner_id':g.user.user_id, 'message': message, 'access_token':g.user.access_token}
            resp = vkontakte.get('wall.post', data)
            if resp.status == 200:
                if resp.data.has_key('response'):
                    result = resp.data['response']
                elif resp.data.has_key('error'):
                    {'error':'Unhandled Exception'}
                else: 
                    result = resp.data['error']
            else:
                result = {'error':'Unhandled Exception'}

        return jsonify(result)
    
    
    
    
class Message(View):

    def __init__(self, template_name):
        self.template_name = template_name
        self.title = _('User messages')

    def render_template(self, context):
        return render_template(self.template_name, **context)

    def dispatch_request(self):
        vk_user_info = None
        vk_user_messages = None

        if g.user is not None:
            data = {
                     'uids':g.user.user_id, 
                     'fields': 'uid,first_name,last_name,nickname,screen_name, activity, sex,bdate,city,country,timezone,photo,photo_medium,photo_big,has_mobile,rate,contacts,education,online,counters',
                     'access_token':g.user.access_token,
                   }


            resp = vkontakte.get('users.get', data)
            if resp.status == 200:
                vk_user_info = resp.data['response'][0]
            else:
                flash('Unable to load userinfo from vkontakte. Maybe out of '
                      'API calls or vkontakte is overloaded.')					
						
            data = {
                     'count':5,
                     'access_token':g.user.access_token,
                   }

            resp = vkontakte.get('messages.get', data)
            if resp.status == 200:
                if resp.data.has_key('response'):
                    vk_user_messages = resp.data['response']
                elif resp.data.has_key('error'):
                    vk_user_messages = resp.data['error']
                else: 
                    vk_user_messages = {'error':'Unhandled Exception'}
            else:
                vk_user_messages = {'error':'Unhandled Exception'}

        context = {'user_info':vk_user_info, 'user_messages': vk_user_messages}
        return self.render_template(context)