import webapp2
import jinja2
from models import Event, Profile
from datetime import date
from google.appengine.api import users

env = jinja2.Environment(loader=jinja2.FileSystemLoader('templates'))

class MainHandler(webapp2.RequestHandler):
    def get(self):
        home_template = env.get_template('home.html')
        user = users.get_current_user()
        logout_url = users.create_logout_url('/')
        login_url = users.create_login_url('/')
        if user:
            greeting = ('Welcome, %s! (<a href="%s">sign out</a>)' %
                (user.nickname(), logout_url))
        else:
            greeting = ('<a href="%s">Sign in or register</a>' % login_url)
        vars = {
            'greeting': greeting,
            }
        self.response.write(home_template.render(vars))

class EventsHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        logout_url = users.create_logout_url('/')
        login_url = users.create_login_url('/')
        if user:
            greeting = ('Welcome, %s! (<a href="%s">sign out</a>)' %
                (user.nickname(), logout_url))
        else:
            greeting = ('<a href="%s">Sign in or register</a>' % login_url)
        events = Event.query().fetch(limit=50)
        events_template = env.get_template('events.html')
        self.response.write(events_template.render({ 'events': events, 'greeting': greeting }))

class SubmitEventHandler(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        logout_url = users.create_logout_url('/')
        login_url = users.create_login_url('/')
        if user:
            greeting = ('Welcome, %s! (<a href="%s">sign out</a>)' %
                (user.nickname(), logout_url))
        else:
            greeting = ('<a href="%s">Sign in or register</a>' % login_url)
        vars = {
            'greeting': greeting,
            }
        submit_event_template = env.get_template('submit_event.html')
        self.response.write(submit_event_template.render(vars))

    def post(self):
        event_created_template = env.get_template('event_created.html')
        template_variables= {'event_name': self.request.get('event_name')}
        event = Event(
            event_name=self.request.get('event_name'),
            event_location=self.request.get('event_location'),
            event_date=self.request.get('event_date'),
            event_time=self.request.get('event_time'),
            event_description=self.request.get('event_description'),
            event_category=self.request.get('event_category'),
        )
        key = event.put()
        self.response.write(event_created_template.render(template_variables))

class ProfileHandler(webapp2.RequestHandler):
    def get(self):
        profile_template = env.get_template('profile2.html')
        user = users.get_current_user()
        vars = {
            'name': Profile.name,
            'affiliated_group': Profile.affiliated_group,
            'interests': Profile.interests,
            'gender': Profile.gender,
            'orientation': Profile.orientation,
            'pronouns': Profile.pronouns
        }
        # self.response.write(profile_template.render())

        #
        # if profile:
        #     vars = {
        #         'name': Profile.name,
        #         'affiliated_group': Profile.affiliated_group,
        #         'interests': Profile.interests,
        #         'gender': Profile.gender,
        #         'orientation': Profile.orientation,
        #         'pronouns': Profile.pronouns
        #     }
        # self.response.write(profile_template.render(vars))


        profile = Profile.query(Profile.user_id == user.user_id())
        if profile:
            vars = {
                'profile': profile
            }
        self.response.write(profile_template.render(vars))

    def post(self):
        profile_template = env.get_template('profile2.html')

        user = users.get_current_user()
        profile = Profile.query(Profile.user_id == user.user_id()).get()

        user_id = users.get_current_user().user_id()
        profile = Profile(
            name=self.request.get('name'),
            affiliated_group=self.request.get('affiliated_group'),
            interests=self.request.get('interested_in'),
            gender=self.request.get('gender'),
            orientation=self.request.get('orientation'),
            pronouns=self.request.get('pronouns'),
            user_id=user_id
        )
        profile.put()

        self.response.write(profile_template.render({'profile': profile}))

class EditProfileHandler(webapp2.RequestHandler):
    def post(self):
        profile_template = env.get_template('profileedit.html')
        user = users.get_current_user()
        profile = Profile.query(Profile.user_id == user.user_id())
        if profile:
            vars = {
                'name': Profile.name,
                'affiliated_group': Profile.affiliated_group,
                'interests': Profile.interests,
                'gender': Profile.gender,
                'orientation': Profile.orientation,
                'pronouns': Profile.pronouns
            }
        self.response.write(profile_template.render(vars))



app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/events', EventsHandler),
    ('/submit_event', SubmitEventHandler),
    ('/profile', ProfileHandler),
    ('/event_created', SubmitEventHandler),
    ('/edit_profile', EditProfileHandler)
], debug=True)
