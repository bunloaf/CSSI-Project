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
        search_date = self.request.get('date')
        user = users.get_current_user()
        logout_url = users.create_logout_url('/')
        login_url = users.create_login_url('/')
        if user:
            greeting = ('Welcome, %s! (<a href="%s">sign out</a>)' %
                (user.nickname(), logout_url))
        else:
            greeting = ('<a href="%s">Sign in or register</a>' % login_url)

        if (search_date):
            day_after_search_date = search_date[:-1] + chr(ord(search_date[-1])+1)
            print search_date
            print day_after_search_date
            events = Event.query(Event.event_date >= search_date,
                Event.event_date < day_after_search_date).order(-Event.event_date).fetch(limit=50)
        else:
            events = Event.query().order(-Event.event_date).fetch(limit=50)
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
            'profile': {}
        }

        profile_template = env.get_template('profile2.html')
        user = users.get_current_user()
        vars = {
            'name': Profile.name,
            'affiliated_group': Profile.affiliated_group,
            'interests': Profile.interests,
            'gender': Profile.gender,
            'orientation': Profile.orientation,
            'pronouns': Profile.pronouns,
            'bio' : Profile.bio or ''
        }


        profile = Profile.query(Profile.user_id == user.user_id()).get()
        if profile == None:
            profile = Profile(
                name=users.get_current_user().nickname(),
                user_id=user.user_id()
            )
            profile.put()
        vars = {
            'profile': {
                'name': profile.name,
                'affiliated_group': profile.affiliated_group or '',
                'interests': profile.interests or '',
                'gender': profile.gender or '',
                'orientation': profile.orientation or '',
                'pronouns': profile.pronouns or '',
                'bio': profile.bio or ''
            }
        }
        self.response.write(profile_template.render(vars))

    def post(self):
        profile_template = env.get_template('profile2.html')

        user = users.get_current_user()
        profile = Profile.query(Profile.user_id == user.user_id()).get()

        user_id = users.get_current_user().user_id()

        profile.name = self.request.get('name') or profile.name
        profile.affiliated_group = self.request.get('affiliated_group') or profile.affiliated_group
        profile.interests = self.request.get('interests') or profile.interests
        profile.gender = self.request.get('gender') or profile.gender
        profile.orientation = self.request.get('orientation') or profile.orientation
        profile.pronouns = self.request.get('pronouns') or profile.pronouns

        profile.bio = self.request.get('bio') or profile.bio


        profile.put()

        self.response.write(profile_template.render({'profile': profile}))

class EditProfileHandler(webapp2.RequestHandler):
    def post(self):
        user = users.get_current_user()
        logout_url = users.create_logout_url('/')
        login_url = users.create_login_url('/')
        if user:
            greeting = ('Welcome, %s! (<a href="%s">sign out</a>)' %
                (user.nickname(), logout_url))
        else:
            greeting = ('<a href="%s">Sign in or register</a>' % login_url)

        profile_template = env.get_template('profileedit.html')
        user = users.get_current_user()
        profile = Profile.query(Profile.user_id == user.user_id()).get()
        vars = {
            'name': profile.name,
            'affiliated_group': profile.affiliated_group or '',
            'interests': profile.interests or '',
            'gender': profile.gender or '',
            'orientation': profile.orientation or '',
            'pronouns': profile.pronouns or '',
            'bio': profile.bio or ''
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
