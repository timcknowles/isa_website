from django.db import models

from django import forms
from django.shortcuts import render
from django.template.response import TemplateResponse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel, FieldRowPanel, MultiFieldPanel, InlinePanel
from wagtail.search import index
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase
from wagtail.snippets.models import register_snippet
from wagtail.images.edit_handlers import ImageChooserPanel



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

@register_snippet
class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(
        verbose_name="slug",
        allow_unicode=True,
        max_length=255,
        help_text='A slug to identify posts by this category',
        null=True,
    )
    icon = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )

    panels = [
        FieldPanel('name'),
        FieldPanel('slug'),
        ImageChooserPanel('icon'),
    ]

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ["name"]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'categories'

class NewsIndexPage(RoutablePageMixin, Page):
    intro = RichTextField(blank=True)
    thanks_info = RichTextField(blank=True)

    def children(self):
        return self.get_children().specific().live()


    def get_context(self, request):
        context = super(NewsIndexPage, self).get_context(request)
        context['posts'] = NewsPage.objects.descendant_of(
            self).live().order_by('-first_published_at')
        context["categories"] = Category.objects.all()
        child_pages = NewsPage.objects.descendant_of(
            self).live().order_by('-first_published_at')

        paginator = Paginator(child_pages, 4)
        # Try to get the ?page=x value
        page = request.GET.get("page")
        try:
            # If the page exists and the ?page=x is an int
            posts = paginator.page(page)
        except PageNotAnInteger:
            # If the ?page=x is not an int; show the first page
            posts = paginator.page(1)
        except EmptyPage:
            # If the ?page=x is out of range (too high most likely)
            # Then return the last page
            posts = paginator.page(paginator.num_pages)

        # "posts" will have child pages; you'll need to use .specific in the template
        # in order to access child properties, such as youtube_video_id and subtitle
        context["posts"] = posts



        return context



    # @route(r'^category/(?P<category>[-\w]+)/$')
    # def post_by_category(self, request, category, *args, **kwargs):
    #     context = self.get_context(request, *args, **kwargs)
    #     posts = NewsDetailPage.objects.live().public().filter(categories__slug=category)
    #
    #     context["posts"] = posts
    #     context["categories"] = Category.objects.all()
    #     context["search_term"] = category
    #     return render(request, self.template, context)







    # @route(r'^category/(?P<category>[-\w]+)/$')
    # def post_by_category(self, request, category, *args, **kwargs):
    #     context = super().get_context(request)
    #     newspages = self.get_children().live().order_by('-first_published_at')
    #     context['newspages'] = newspages
    #     context["categories"] = Category.objects.all()
    #
    #
    #     return context
    @route(r'^category/(?P<category>[-\w]+)/$')
    def post_by_category(self, request, category, *args, **kwargs):
        context = self.get_context(request, *args, **kwargs)
        posts = NewsPage.objects.live().public().filter(categories__slug__in=[category])

        child_pages = posts

        paginator = Paginator(child_pages, 2)
        # Try to get the ?page=x value
        page = request.GET.get("page")
        try:
            # If the page exists and the ?page=x is an int
            posts = paginator.page(page)
        except PageNotAnInteger:
            # If the ?page=x is not an int; show the first page
            posts = paginator.page(1)
        except EmptyPage:
            # If the ?page=x is out of range (too high most likely)
            # Then return the last page
            posts = paginator.page(paginator.num_pages)

        # "posts" will have child pages; you'll need to use .specific in the template
        # in order to access child properties, such as youtube_video_id and subtitle


        # context['newspages'] = newspages
        context["posts"] = posts
        context["search_term"] = category
        return render(request, self.template, context)
        # this works too
        # return Page.serve(self, request, *args, **kwargs)
    @route(r'^$')
    def base(self, request):
        return TemplateResponse(
          request,
          self.get_template(request),
          self.get_context(request)
        )

    @route(r'^submit-blog/$')
    def submit(self, request):
        from .views import submit_blog
        return submit_blog(request, self)

    @route(r'^submit-thank-you/$')
    def thanks(self, request):
        return TemplateResponse(
          request,
           'thank_you.html',
           { "thanks_info" : self.thanks_info }
        )

    # parent_page_types = []

    content_panels = Page.content_panels + [
        FieldPanel('thanks_info', classname="full"),

]
class NewsPage(Page):
    intro = models.CharField('one line summary', max_length=250, blank=True)
    summary = RichTextField(blank=True, verbose_name="summary")
    first_name = models.CharField('First name', max_length=250, blank=True)
    last_name = models.CharField('Last name', max_length=250, blank=True)
    email = models.EmailField('email', blank=True)
    contact_number = models.CharField('number', max_length=250, blank=True)
    publish_to_twitter = models.BooleanField(default=False, verbose_name="Publish to Twitter?")
    categories = ParentalManyToManyField('news.Category', blank=True)


    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('summary'),
        index.SearchField('categories'),
    ]

    parent_page_types = ['NewsIndexPage']



    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full"),
        FieldPanel('summary', classname="full"),
        FieldPanel('publish_to_twitter', widget=forms.CheckboxInput),

     MultiFieldPanel([
            FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
        ], heading="Blog information"),



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
