from django import template
from home.models import Event

register = template.Library()

...

# Advert snippets
@register.inclusion_tag('home/tags/event.html', takes_context=True)
def event(context):
    return {
        'event': Event.objects.all().filter(event_code="core"),
        # 'event' : Event.objects.all().filter(event_code="core"),
        # 'event' : Event.objects.all().filter(event_code="higher"),

        'request': context['request'],
    }


# context= {
#     "coreevents": core_events,
#     "intermediates": int_events,
#     "higher_events": higher_events,
#     "other_events": other_events
# }
