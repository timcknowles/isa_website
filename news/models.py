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

class NewsIndexPage(Page):
    intro = RichTextField(blank=True)

    def get_context(self, request):
            # Update context to include only published posts, ordered by reverse-chron
            context = super().get_context(request)
            newspages = self.get_children().live().order_by('-first_published_at')
            context['newspages'] = newspages
            return context

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

    # parent_page_types = []


class NewsPage(Page):
    intro = models.CharField('one line summary', max_length=250)
    summary = RichTextField('full summary')
    first_name = models.CharField('First name', max_length=250, blank=True)
    last_name = models.CharField('Last name', max_length=250, blank=True)
    email = models.EmailField('email', blank=True)
    contact_number = models.CharField('number', max_length=250, blank=True)
    publish_to_twitter = models.BooleanField(default=False, verbose_name="Check box to publish to Twitter")

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('summary'),
    ]

    parent_page_types = ['NewsIndexPage']

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full"),
        FieldPanel('summary', classname="full"),
        FieldPanel('publish_to_twitter', classname="full"),

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
