#!/usr/bin/env python
# -*- coding: utf-8 -*-

import functools
from datetime import datetime

from flask import Response
from flask import _request_ctx_stack, g, request
from google.appengine.ext import db

from vksunshine.extensions import cache

# try to load the best simplejson implementation available.  If JSON
# is not installed, we add a failing class.
json_available = True
json = None
try:
    import simplejson as json
except ImportError:
    try:
        import json
    except ImportError:
        try:
            # Google Appengine offers simplejson via django
            from django.utils import simplejson as json
        except ImportError:
            json_available = False


cached = functools.partial(cache.cached,
                           unless= lambda: g.user is not None)

def url_for2(endpoint, **values):
    """Overriden method to always add request.view_args."""

    if endpoint != '.static':
        values.update(request.view_args)

    # The code below is from flask.url_for
    ctx = _request_ctx_stack.top
    if '.' not in endpoint:
        mod = ctx.request.module
        if mod is not None:
            endpoint = mod + '.' + endpoint
    elif endpoint.startswith('.'):
        endpoint = endpoint[1:]
    external = values.pop('_external', False)
    return ctx.url_adapter.build(endpoint, values, force_external=external)


def slugify(text, delim=u'-'):
    """Generates an ASCII-only slug. From http://flask.pocoo.org/snippets/5/"""
    result = []
    for word in _punct_re.split(text.lower()):
        #word = word.encode('translit/long')
        if word:
            result.append(word)
    return unicode(delim.join(result))
 
def dumps(obj):
    if isinstance(obj, str):
        return str(obj)
    elif obj == None:
        return None
    elif isinstance(obj, list):
        items = [];
        for item in obj:
            items.append(dumps(item))
        return items
    elif isinstance(obj, datetime):
        return obj.ctime()
    properties = dict();
    if isinstance(obj, db.Model):
        properties['kind'] = obj.kind()
        properties['key']  = str(obj.key())
    for property in dir(obj):
        if property[0] != '_':
            try:
                value = obj.__getattribute__(property)
                valueClass = str(value.__class__)
                if not(('function' in valueClass) or ('built' in valueClass) or ('method' in valueClass)):
                    value = dumps(value)
                    if value != None:
                        properties[property] = value
                    else:
                        properties[property] = ""
            except: continue
    if len(properties) == 0:
        return str(obj)
    else:
        return properties

class JSONModelEncoder(json.JSONEncoder):
    def default(self, o):
        """jsonify default encoder"""
        return dumps(o)

def jsonify(data, **kwargs):
    """jsonify data in a standard (human friendly) way. If a db.Model
    entity is passed in it will be encoded as a dict.
    """
    json_result = json.dumps(data, skipkeys=True, sort_keys=True,
                            ensure_ascii=False,indent=4, cls=JSONModelEncoder).replace('\\', '')
    return Response(json_result, mimetype='application/json')