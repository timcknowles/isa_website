from django.db import models

# Create your models here.
from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, FieldRowPanel, MultiFieldPanel, InlinePanel
from wagtail.search import index

# Create your models here.

# class PersonBlock(blocks.StructBlock):
#     job_title = blocks.CharBlock()
#     first_name = blocks.CharBlock()
#     last_name = blocks.DecimalBlock()
#     contact_number = blocks.CharBlock()
#     email = blocks.EmailBlock()
#
#
#
#     class Meta:
#         template = 'blocks/person_block.html'

class SurveysIndexPage(Page):
    intro = RichTextField(blank=True)

    def get_context(self, request):
            # Update context to include only published posts, ordered by reverse-chron
            context = super().get_context(request)
            surveypages = self.get_children().live().order_by('-first_published_at')
            context['surveypages'] = surveypages
            return context

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

    # parent_page_types = []

class SurveysPage(Page):
    intro = models.CharField('one line summary', max_length=250)
    summary = RichTextField('full summary')
    survey_url = models.URLField('link to survey')
    first_name = models.CharField('First name', max_length=250, blank=True)
    last_name = models.CharField('Last name', max_length=250, blank=True)
    email = models.EmailField('email', blank=True)
    contact_number = models.CharField('number', max_length=250, blank=True)


    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('summary'),
    ]

    parent_page_types = ['SurveysIndexPage']

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full"),
        FieldPanel('summary', classname="full"),
        FieldPanel('survey_url', classname="full"),


    MultiFieldPanel(
    [
        FieldPanel('first_name', classname="full"),
        FieldPanel('last_name', classname="full"),
        FieldPanel('email', classname="full"),
        FieldPanel('contact_number', classname="full")


    ],
    heading="posted by:",
    # classname="collapsible collapsed"
    ),
]
