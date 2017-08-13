from google.appengine.ext import ndb

class User(ndb.Model):
    real_name=ndb.StringProperty()
    screen_name=ndb.StringProperty()
    user_email=ndb.StringProperty()
    user_password=ndb.StringProperty()
