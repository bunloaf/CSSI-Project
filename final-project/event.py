from google.appengine.ext import ndb

class Event(ndb.Model):
    event_name = ndb.StringProperty()
    event_location = ndb.StringProperty()
    event_date = ndb.StringProperty()
    event_description = ndb.StringProperty()
    event_category = ndb.StringProperty()
