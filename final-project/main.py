import webapp2
import jinja2
from event import Event
from user import User
import datetime

env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        template = env.get_template('home.html')
        self.response.write(template.render('home.html'))

class CreateEventHandler(webapp2.RequestHandler):
    def get(self):
        create_event_template = env.get_template('create_event.html')
        self.response.write(create_event_template.render())

    def post(self):
        event_created_template = env.get_template('event_created.html')
        self.response.write(event_created_template.render())
        event = Event(
            event_name=self.request.get('event_name'),
            event_location=self.request.get('event_location'),
            event_date=datetime.date(
                int(self.request.get('event_year')),
                int(self.request.get('event_month')),
                int(self.request.get('event_day'))),
            event_description=self.request.get('event_description'),
            event_category=self.request.get('event_category')
        )

class CreateUserHandler(webapp2.RequestHandler):
    def get(self):
        create_user_template = env.get_template('create_user.html')
        self.response.write(create_user_template.render())

    def post(self):
        user_created_template = env.get_template('user_created.html')
        self.response.write(user_created_template.render())
        user = User(
            real_name=self.request.get('real_name'),
            screen_name=self.request.get('screen_name'),
            user_email=self.request.get('user_email'),
            user_password=self.request.get('user_password')
        )

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/create_event', CreateEventHandler),
    ('/create_user', CreateUserHandler),
], debug=True)
