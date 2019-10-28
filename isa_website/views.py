
import datetime
import os
import json
import codecs

from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.utils.dateparse import parse_datetime
from django.db import IntegrityError
from django.shortcuts import render_to_response
from django.core.exceptions import ObjectDoesNotExist

from eventbrite import Eventbrite

# from home.models import Event
from events.models import Event


#set the token
eventtoken = os.environ.get('EVENTBRITE_TOKEN')

#reader to decode the Http
reader = codecs.getreader("utf-8")


def show_events_view(request):
    eventbrite = Eventbrite(eventtoken)
    my_id = eventbrite.get_user()['id']
    events = eventbrite.event_search(**{'user.id': my_id})
    venue_id = '36600409'
    venue_location = eventbrite.get('/venues/{venue_id}'.format(venue_id=venue_id))
    venue_name=(venue_location['name'])
    print(venue_name)

    existing_events = Event.objects.all().values("event_id")
    events_list = []
    for i in existing_events:
        events_list.append(i['event_id'])

    for x in events['events']:
        event_id=(x['id'])

        if event_id in events_list:
            pass
        else:
            start_time=parse_datetime(x['start']['local'])
            api_url=(x['url'])
            event_id=(x['id'])
            venue_id=(x['venue_id'])
            event_url=(x['url'])
            title=(x['name']['html'])
            name_code = title[4:7].lower()
            if name_code == "cor":
                code = "core"
            elif name_code == "int":
                code = "inter"
            elif name_code =="hig":
                code = "higher"

            else:
                code = "other"
            print(event_id)
            print("this is the venue id"+ venue_id)

            print(start_time)
            new_event = Event(api_url=api_url, event_start=start_time, title=title, event_url=api_url, event_code=code, event_id=event_id)
            print(new_event)
            new_event.save()


    context= {

    }

    return render(request,'showevents.html', context)




@csrf_exempt
def eventbrite(request):
    eventbrite = Eventbrite(eventtoken)

    data = request.body.decode('utf-8')
    data  = json.loads(data)

    api_url = data['api_url']



    try:
        api_object = eventbrite.get(api_url)
        print(api_object.pretty)

        start_time = parse_datetime(api_object['start']['local'])

        #find which kind of event it is
        #get first 3 characters of event name ISA Intermediate Training Day
        name_code = api_object['name']['html'][4:7]
        name_code = name_code.lower()

        def add_event(code):
            #ToDo: make sure event isn't already in db
            new_event = Event(api_url=api_url, event_start=start_time, title=api_object['name']['html'], event_url=api_object['url'], event_code=code)
            new_event.save()

        #now loop to put event in correct category
        if name_code == "cor":
            add_event("core")
        elif name_code == "int":
            add_event("inter")
        elif name_code =="hig":
            add_event("higher")
        elif name_code == "fd ":
            #skip faculty development events
            pass
        else:
            add_event("other")

        return HttpResponse("webhook received by ISA")

    except:
        print ("bad api url")
        return HttpResponseBadRequest("bad api url")



# @app.route('/eventbrite', methods=['POST'])
def webhook():

    # Use the API client to convert from a webhook to an API object
    api_object = eventbrite.webhook_to_object(request)

    # Process the API object
    if api_object.type == 'User':
        do_user_process(api_object)

    if api_object.type == 'Event':
        do_event_process(api_object)

    return ""


def event_view(request):
    eventbrite = Eventbrite(eventtoken)
    core_events = Event.objects.all().filter(event_code="core")
    int_events = Event.objects.all().filter(event_code="inter")
    higher_events = Event.objects.all().filter(event_code="higher")
    other_events = Event.objects.all().filter(event_code="other")

    live_events = [[],[],[],[],[]]

    context= {
        "coreevents": core_events,
        "intermediates": int_events,
        "higher_events": higher_events,
        "other_events": other_events
    }

    return render(request,'events.html', context)
