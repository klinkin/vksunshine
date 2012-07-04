from google.appengine.ext import ndb

class User(ndb.Model):

    user_id         = ndb.IntegerProperty()
    access_token    = ndb.StringProperty()
    expires_in      = ndb.IntegerProperty()
    created         = ndb.DateTimeProperty(auto_now_add=True)
    updated         = ndb.DateTimeProperty(auto_now=True)
    last_login_time = ndb.DateTimeProperty()