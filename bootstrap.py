#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import logging
import path_changer

from vksunshine import create_app
from werkzeug_debugger_appengine import get_debugged_app

__all__ = ["application"]


application = create_app()

if 'SERVER_SOFTWARE' in os.environ and os.environ['SERVER_SOFTWARE'].startswith('Dev'):
    application.debug = True
    application = get_debugged_app(application)