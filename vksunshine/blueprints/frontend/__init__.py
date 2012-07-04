#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Blueprint
from urls import get_urls

def configure_routes():
    for url, view_func in get_urls():
        bp.add_url_rule(url, view_func=view_func)

bp = Blueprint('frontend', __name__, template_folder='templates')
configure_routes()

