# -*- coding: utf-8 -*-

# Set secret keys for CSRF protection
SECRET_KEY = 'qPBOCN0Gv4UQC54c0eIfHPJg'
CSRF_SESSION_LKEY = 'BH8x2AAR7DFh44OQY3L1Fz1u'
CSRF_ENABLED = True

#----------------------MEDIA--------------------------------------------
STATIC_URL = '/static'

#----------------------CACHE--------------------------------------------
CACHE_TYPE            = 'gaememcached'
CACHE_DEFAULT_TIMEOUT = 300

#----------------------BABEL--------------------------------------------
BABEL_DEFAULT_LOCALE   = 'ru_Ru'
BABEL_DEFAULT_TIMEZONE = 'UTC+4'

LANGUAGE_NAMES = { u'de': u'Deutsch',
                   u'en': u'English',
                   u'ru': u'Russian',
                 }

#-----------------------GOOGLE ANALYTICS--------------------------------
ANALYTICS_ID = "######################"

#---------------------GAEMiniProfiler-----------------------------------
GAEMINIPROFILER_PROFILER_ENABLED = False
GAEMINIPROFILER_PROFILER_ADMINS  = True
GAEMINIPROFILER_PROFILER_EMAILS  = ['admin@gmail.com',]

#---------------------USERENA_SETTINGS----------------------------------
#USERENA_AUTH_BACKEND    = 'gae'
#USERENA_AUTH_USER_MODEL = 'gae'
#USERENA_AUTH_FORMS      = 'gae'

#---------------------SEASURF_SETTINGS----------------------------------
SEASURF_INCLUDE_OR_EXEMPT_VIEWS = 'include'


#--------------------VK------------------------------------
#Production
VK_CONSUMER_KEY = '3014832'
VK_CONSUMER_SECRET = 'cUkb0LwIs98HoBqqmU6D'

#Local dev
#VK_CONSUMER_KEY = '3025017'
#VK_CONSUMER_SECRET = 'PgjrxPjHh00TZ2M8g7k3'

#Local dev desktop
#VK_CONSUMER_KEY = '3033820'
#VK_CONSUMER_SECRET = 'rSsyg52WFN4GVOgqZ1bO'

VK_BASE_URL = 'https://api.vk.com/method/'
VK_REQUEST_TOKEN_PARAMS = {'display': 'popup', 'scope': 'friends,video,offline'}
VK_ACCESS_TOKEN_URL='https://oauth.vk.com/access_token'
VK_AUTHORIZE_URL = 'http://api.vk.com/oauth/authorize'