import os

from django.core.management.base import BaseCommand
from django.utils.dateparse import parse_datetime

from eventbrite import Eventbrite

from home.models import Event

#51512751025

class Command(BaseCommand):
    help = 'manually adds eventbrite event to the db'

    def handle(self, *args, **options):
        eventtoken = os.environ.get('EVENTBRITE_TOKEN')
        eventbrite = Eventbrite(eventtoken)

        event_ID = input("Please enter the ID of the event you would like to manually add: ")

        api_object = eventbrite.get("/events/{0}".format(event_ID))
        #print(api_object.pretty)
        #get the api_url to avoid an error
        api_url=api_object['resource_uri']

        #parse time because dates are horrible
        start_time = parse_datetime(api_object['start']['local'])

        #find which kind of event it is
        #get first 3 characters of event name
        name_code = api_object['name']['html'][0:3]
        name_code = name_code.lower()

        print('do you want to add the following event? \n Title: ', api_object['name']['html'], '\n Start Date:', start_time, '\n Y/N')

        decision = input().lower()

        if decision == 'y':
            print("adding...")
            def add_event(code):
                #todo: import this function from isa_website/views
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
        else:
            print("ok thx bye")
