from django.http import HttpResponse
from wagtail.core import hooks
from .models import EventbritePage, HomePage, EventPage
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
    if Page.specific_class == EventbritePage:
        user = eventbrite.get('/users/me/owned_events')
        print (user.pretty)
        # return HttpResponse("Congrats on making content!", content_type="text/plain")
        # startime = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
        # print (startime)
        startime = Page.event_start
        # startime = datetime.datetime.utcnow() + datetime.timedelta(hours=1)
        startime = startime.strftime('%Y-%m-%dT%H:%M:%SZ')
        # endtime = datetime.datetime.utcnow().isoformat()+ datetime.timedelta(hours=2)
        print(startime)

        endtime = Page.event_end
        # endtime = datetime.datetime.utcnow() + datetime.timedelta(hours=2)
        endtime = endtime.strftime('%Y-%m-%dT%H:%M:%SZ')
        title = Page.title
        description = Page.event_description

        # return self.post("/events/{0}/".format(id), data=data)
        myevent = {"event":{
            "name" : {'html':(title)},
            "start" : {
                'utc': str(startime),
                'timezone': 'Europe/London'
                } ,
            "end" : {
                'utc': str(endtime),
                'timezone': 'Europe/London'
                } ,
            "currency" : 'GBP',



            "description" : {'html':(description)},


        }}



        postevent = eventbrite.post_event(myevent)
        # postticketdata = eventbrite.post_event_ticket_class([postevent.id],data=ticket_data)
        tickets = eventbrite.post_event_ticket_class(postevent.id, {
                'ticket_class.name': 'Free',
                'ticket_class.free': True,
                'ticket_class.minimum_quantity': 1,
                'ticket_class.maximum_quantity': 1,
                'ticket_class.quantity_total': 10,
            })

        publishevent = eventbrite.publish_event(postevent.id)

        print (tickets)
        print (postevent)

        print (publishevent)



        return HttpResponse("Congrats on making an event", content_type="text/plain")


@hooks.register('before_serve_page')
def get_eventbrite_events(page, request, args, kwargs):
    if page.specific_class == EventPage:
        print (page.pretty)
