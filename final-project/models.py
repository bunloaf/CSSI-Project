from google.appengine.ext import ndb

class Event(ndb.Model):
    event_name = ndb.StringProperty()
    event_location = ndb.StringProperty()
    event_date = ndb.StringProperty()
    event_description = ndb.StringProperty()
    event_category = ndb.StringProperty()

class User(ndb.Model):
    real_name=ndb.StringProperty()
    screen_name=ndb.StringProperty()
    user_email=ndb.StringProperty()
    user_password=ndb.StringProperty()
