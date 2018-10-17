from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import StreamField
from wagtail.core import blocks
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.search import index


# Create your models here.
class CourseIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]


class CoursePage(Page):
    intro = models.CharField(max_length=250)
    details = StreamField([
        ('heading', blocks.CharBlock()),
        ('summary', blocks.RichTextBlock()),
        ('link', blocks.URLBlock()),
    ])

    dates = StreamField([
        ('start_date', blocks.DateTimeBlock()),
        ('end_date', blocks.DateTimeBlock()),
        ('date_list', blocks.ListBlock(blocks.DateBlock())),
    ])

    documents = StreamField([
        ('document', DocumentChooserBlock()),

    ])

    person = StreamField([
        ('name', blocks.CharBlock()),
        ('email', blocks.EmailBlock()),
        ('number', blocks.CharBlock()),

    ])

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('details'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        StreamFieldPanel('details'),
        StreamFieldPanel('dates'),
        StreamFieldPanel('documents'),
        StreamFieldPanel('person'),

    ]
