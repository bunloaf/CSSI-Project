import webapp2
import jinja2
from event import Event
import datetime

env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('home.html')
        self.response.write(template.render('home.html'))

class CreateEventHandler(webapp2.RequestHandler):
    def get(self):
        event = Event(
            name=self.request.get('event_name'),
            location=self.request.get('event_location'),
            date=datetime.date(
                int(self.request.get('event_year')),
                int(self.request.get('event_month')),
                int(self.request.get('event_day'))),
            description=self.request.get('event_description'),
            category=self.request.get('event_category'))
        self.response.write('You created the event: ' + event.name)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/create_event', CreateEventHandler),
], debug=True)
