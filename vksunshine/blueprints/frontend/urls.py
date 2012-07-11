#!/usr/bin/env python
# -*- coding: utf-8 -*-

from vksunshine.blueprints.frontend.views import *

def get_urls():
    return (
        ('',  Home.as_view('promo', template_name='promo.html')),
        ('/', Home.as_view('promo', template_name='promo.html')),
        ('messages', Message.as_view('message', template_name='messages.html')),
        ('news', News.as_view('news', template_name='news.html')),
        ('addnews', AddNews.as_view('addnews')),
        
    )