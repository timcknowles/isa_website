from django.http import HttpResponse
from wagtail.core import hooks
from .models import EventPage, HomePage
from eventbrite import Eventbrite
import os
import datetime
import json
from django.core.serializers.json import DjangoJSONEncoder

#set the token
eventtoken = os.environ.get('EVENTBRITE_TOKEN')
eventbrite = Eventbrite(eventtoken)



@hooks.register('after_create_page')
def do_after_page_create(request, Page):
    if Page.specific_class == EventPage:
        user = eventbrite.get('/users/me/owned_events')
        print (user.pretty)
        # return HttpResponse("Congrats on making content!", content_type="text/plain")
        # startime = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
        # print (startime)
        startime = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        startime = startime.strftime('%Y-%m-%dT%H:%M:%SZ')
        # endtime = datetime.datetime.utcnow().isoformat()+ datetime.timedelta(hours=2)
        endtime = datetime.datetime.utcnow() + datetime.timedelta(hours=2)
        endtime = endtime.strftime('%Y-%m-%dT%H:%M:%SZ')

        # return self.post("/events/{0}/".format(id), data=data)
        myevent = {"event":{
            "name" : {'html':'testtest'},
            "start" : {
                'utc': str(startime),
                'timezone': 'Europe/London'
                } ,
            "end" : {
                'utc': str(endtime),
                'timezone': 'Europe/London'
                } ,
            "currency" : 'GBP',

        }}
        # my_event = json.dumps(myevent, indent=4, sort_keys=True, default=str)

        postevent = eventbrite.post_event(myevent)

    
        print (postevent)

        return HttpResponse("Congrats on making an event", content_type="text/plain")
