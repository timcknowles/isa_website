from django.db import models
from wagtail.admin.edit_handlers import (
    FieldPanel,
    StreamFieldPanel,
    InlinePanel,
    MultiFieldPanel,
    FieldRowPanel,
)
from events.models import Event
from wagtail.snippets.models import register_snippet


@register_snippet
class Certificate(models.Model):
    event_id = models.ForeignKey("events.Event", blank=True, on_delete=models.CASCADE)
    attendee_name = models.CharField(max_length=255, blank=True)
    email_address = models.CharField(max_length=255, blank=True)
    attended = models.BooleanField(max_length=255, blank=True)
    feedback_complete = models.BooleanField(max_length=255, blank=True, default=False)

    panels = [
        FieldPanel("event_id"),
        FieldPanel("attendee_name"),
        FieldPanel("email_address"),
        FieldPanel("attended"),
        FieldPanel("feedback_complete"),
    ]

    # base_form_class = EventForm

    # def __str__(self):
    #     return self.title
