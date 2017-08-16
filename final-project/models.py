from google.appengine.ext import ndb

class Event(ndb.Model):
    event_name = ndb.StringProperty()
    event_location = ndb.StringProperty()
    event_date = ndb.StringProperty()
    event_description = ndb.StringProperty()
    event_category = ndb.StringProperty()

class Profile(ndb.Model):
    name = ndb.StringProperty()
    affiliated_group = ndb.StringProperty()
    interests = ndb.StringProperty()
    gender = ndb.StringProperty()
    orientation = ndb.StringProperty()
    pronouns = ndb.StringProperty()
    user_id = ndb.StringProperty()
