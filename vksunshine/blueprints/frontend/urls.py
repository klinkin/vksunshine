#!/usr/bin/env python
# -*- coding: utf-8 -*-

from vksunshine.blueprints.frontend.views import *

def get_urls():
    return (
        ('',  Home.as_view('promo', template_name='promo.html')),
        ('/', Home.as_view('promo', template_name='promo.html')),
    )