from django.db import models

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, InlinePanel, MultiFieldPanel, FieldRowPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.contrib.table_block.blocks import TableBlock
from wagtail.documents.edit_handlers import DocumentChooserPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.embeds.blocks import EmbedBlock
from wagtail.snippets.models import register_snippet
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.snippets.blocks import SnippetChooserBlock
from wagtail.core.blocks import (CharBlock, ChoiceBlock, RichTextBlock, StreamBlock, StructBlock, TextBlock,)

from modelcluster.fields import ParentalKey

@register_snippet
class Person(models.Model):
    role = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    bio = models.CharField(max_length=255)
    person_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    class Meta:
        verbose_name = "person"
        verbose_name_plural = "people"

    panels = [
        MultiFieldPanel([
            FieldRowPanel([
                FieldPanel('first_name', classname="col6"),
                FieldPanel('last_name', classname="col6"),
            ])
        ], "Name"),
        FieldPanel('role'),
        FieldPanel('bio'),
        ImageChooserPanel('person_image')
    ]
    # panels = [
    #     FieldPanel('role'),
    #     FieldPanel('first_name'),
    #     FieldPanel('last_name'),
    #     FieldPanel('bio'),
    #     ImageChooserPanel('person_image'),
    # ]

    def __str__(self):
        return self.role

class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]

class StandardPagePersonPlacement(Orderable, models.Model):
    page = ParentalKey('StandardPage', on_delete=models.CASCADE, related_name='person_placements')
    person = models.ForeignKey('Person', on_delete=models.CASCADE, related_name='+')

    class Meta:
        verbose_name = "person placement"
        verbose_name_plural = "people placement"

    panels = [
        SnippetChooserPanel('person'),
    ]

    def __str__(self):
        return self.page.title + " -> " + self.people.text

class HeadingBlock(StructBlock):
    """
    Custom `StructBlock` that allows the user to select h2 - h4 sizes for headers
    """
    heading_text = CharBlock(classname="title", required=True)
    size = ChoiceBlock(choices=[
        ('', 'Select a header size'),
        ('h2', 'H2'),
        ('h3', 'H3'),
        ('h4', 'H4')
    ], blank=True, required=False)

    class Meta:
        icon = "title"
        template = "blocks/heading_block.html"

class StandardPage(Page):

    section = StreamField([
        ('heading', HeadingBlock()),
        ('paragraph', blocks.RichTextBlock()),
        ('quote', blocks.BlockQuoteBlock()),
        ('image', ImageChooserBlock()),
        ('document', DocumentChooserBlock()),
        ('embed', EmbedBlock()),
        ('table', TableBlock()),
        ('person', SnippetChooserBlock(Person)),
    ], blank=True)

    person = models.ForeignKey(
        'Person',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )


    content_panels = Page.content_panels + [
        StreamFieldPanel('section'),
        InlinePanel('person_placements', label="people"),


    ]



class EventPage(Page):
    eventname = models.CharField(max_length=255)
    date = models.DateField("event date")
    body = StreamField([
        ('event', blocks.CharBlock(classname="event name")),
        ('description', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
    ])

    content_panels = Page.content_panels + [
        FieldPanel('eventname'),
        FieldPanel('date'),
        StreamFieldPanel('body'),
    ]

class EventbritePage(Page):
    event_description = RichTextField(blank=True)
    event_start = models.DateTimeField("event start")
    event_end = models.DateTimeField("event end")


    content_panels = Page.content_panels + [

        FieldPanel('event_start'),
        FieldPanel('event_end'),
        FieldPanel('event_description'),
    ]

#model for events

class Event(models.Model):
    api_url = models.CharField(max_length=255)
    event_start = models.DateTimeField(null=True)
    event_code = models.CharField(max_length=255, blank=True)
    event_url = models.CharField(max_length=255, blank=True)
    title   = models.CharField(max_length=255, blank=True)
