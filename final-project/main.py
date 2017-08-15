import webapp2
import jinja2
from models import Event, User
from datetime import date

env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        home_template = env.get_template('home.html')
        self.response.write(home_template.render())

class AboutHandler(webapp2.RequestHandler):
    def get(self):
        about_template = env.get_template('about.html')
        self.response.write(about_template.render())

class EventsHandler(webapp2.RequestHandler):
    def get(self):
        events = Event.query().fetch(limit=20)
        events_template = env.get_template('events.html')
        self.response.write(events_template.render({ 'events': events }))


class SubmitEventHandler(webapp2.RequestHandler):
    def get(self):
        submit_event_template = env.get_template('submit_event.html')
        self.response.write(submit_event_template.render())

    def post(self):
        event_created_template = env.get_template('event_created.html')
        template_variables= {'event_name': self.request.get('event_name')}
        event = Event(
            event_name=self.request.get('event_name'),
            event_location=self.request.get('event_location'),
            event_date=self.request.get('event_date'),
            event_description=self.request.get('event_description'),
            event_category=self.request.get('event_category'),
        )
        key = event.put()
        self.response.write(event_created_template.render(template_variables))

class ProfileHandler(webapp2.RequestHandler):
    def get(self):
        profile_template = env.get_template('profile.html')
        self.response.write(profile_template.render())

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/about', AboutHandler),
    ('/events', EventsHandler),
    ('/submit_event', SubmitEventHandler),
    ('/profile', ProfileHandler),
    ('/event_created', SubmitEventHandler)
], debug=True)
