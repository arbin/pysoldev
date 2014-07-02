from django.shortcuts import render_to_response
from django.template import RequestContext
from socialregistration.contrib.facebook.models import FacebookProfile
from socialregistration.contrib.foursquare.models import FoursquareProfile
from socialregistration.contrib.github.models import GithubProfile
from socialregistration.contrib.instagram.models import InstagramProfile
from socialregistration.contrib.linkedin.models import LinkedInProfile
from socialregistration.contrib.openid.models import OpenIDProfile
from socialregistration.contrib.tumblr.models import TumblrProfile
from socialregistration.contrib.twitter.models import TwitterProfile

class Facebook(object):
    def __init__(self, user=None):
        if user is None:
            self.uid = None
        else:
            self.uid = user['uid']
            self.user = user
            self.graph = facebook.GraphAPI(user['access_token'])

def index(request):    
    return render_to_response(
            'home.html', dict(
                facebook=FacebookProfile.objects.all(),
                twitter=TwitterProfile.objects.all(),
                openid=OpenIDProfile.objects.all(),
                linkedin=LinkedInProfile.objects.all(),
                github=GithubProfile.objects.all(),
                foursquare=FoursquareProfile.objects.all(),
                tumblr=TumblrProfile.objects.all(),
                instagram=InstagramProfile.objects.all(),                
        ), context_instance=RequestContext(request))
								