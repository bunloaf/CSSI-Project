import webapp2
import jinja2
from models import Event, User 
from datetime import date

env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        home_template = env.get_template('home.html')
        self.response.write(home_template.render())

class CreateEventHandler(webapp2.RequestHandler):
    def get(self):
        create_event_template = env.get_template('create_event.html')
        self.response.write(create_event_template.render())

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

class CreateUserHandler(webapp2.RequestHandler):
    def get(self):
        create_user_template = env.get_template('create_user.html')
        self.response.write(create_user_template.render())

    def post(self):
        user_created_template = env.get_template('user_created.html')
        template_variables= {'real_name': self.request.get('real_name')}
        user = User(
            real_name=self.request.get('real_name'),
            screen_name=self.request.get('screen_name'),
            user_email=self.request.get('user_email'),
            user_password=self.request.get('user_password'),
        )
        key = user.put()
        self.response.write(user_created_template.render(template_variables))

class EventsFeedHandler(webapp2.RequestHandler):
    def get(self):
        events_feed_template = env.get_template('events_feed.html')
        self.response.write(events_feed_template.render())



app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/create_event', CreateEventHandler),
    ('/create_user', CreateUserHandler),
    ('/events_feed', EventsFeedHandler),
], debug=True)
