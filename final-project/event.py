from google.appengine.ext import ndb

class Event(ndb.Model):
    name = ndb.StringProperty()
    location = ndb.StringProperty()
    date = ndb.DateProperty()
    description = ndb.StringProperty()
    category = ndb.StringProperty()
