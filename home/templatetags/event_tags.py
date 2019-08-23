from django import template
from home.models import Event

register = template.Library()

...

# event snippets
@register.inclusion_tag('home/tags/event.html', takes_context=True)


def event(context):


    return {
        'event': Event.objects.all().order_by('event_start'),
        'request': context['request'],

    }

# def core(context):
#
#
#     return {
#         'core': Event.objects.all().filter(event_code="core"),
#
#
#
#         'request': context['request'],
#     }

# context= {
#     "coreevents": core_events,
#     "intermediates": int_events,
#     "higher_events": higher_events,
#     "other_events": other_events
# }
