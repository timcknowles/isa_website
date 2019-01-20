import datetime
import os
import json
import codecs

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.utils.dateparse import parse_datetime

from eventbrite import Eventbrite

from home.models import Event

#set the token
eventtoken = os.environ.get('EVENTBRITE_TOKEN')

#reader to decode the Http
reader = codecs.getreader("utf-8")

@csrf_exempt
def eventbrite(request):
    eventbrite = Eventbrite(eventtoken)

    data = request.body.decode('utf-8')
    data  = json.loads(data)

    api_url = data['api_url']

    try:
        api_object = eventbrite.get(i.api_url)
        print(api_object.pretty)

        start_time = parse_datetime(api_object['start']['local'])

        #find which kind of event it is
        #get first 3 characters of event name
        name_code = api_object['name']['html'][0:3]
        name_code = name_code.lower()

        def add_event(code):
            new_event = Event(api_url=api_url, start=start_time, title=api_object['name']['html'], url=api_object['url'], event_code=code)
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

    except:
        print ("bad api url")

    return HttpResponse("webhook received by ISA")


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
    events = Event.objects.all()

    live_events = [[],[],[],[],[]]

    context= {"events": live_events}
    return render(request,'events.html', context)
