from django.db import models
from wagtail.snippets.models import register_snippet
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, InlinePanel, MultiFieldPanel, FieldRowPanel



@register_snippet
class Event(models.Model):
    api_url = models.CharField(max_length=255)
    event_start = models.DateTimeField(null=True)
    event_code = models.CharField(max_length=255, blank=True)
    event_url = models.CharField(max_length=255, blank=True)
    title = models.CharField(max_length=255, blank=True)
    event_id = models.CharField(max_length=255, blank=True)

    panels = [

        FieldPanel('api_url'),
        FieldPanel('event_start'),
        FieldPanel('event_code'),
        FieldPanel('title')


    ]

    # base_form_class = EventForm

    def __str__(self):
        return self.title
