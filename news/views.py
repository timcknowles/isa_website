
import datetime
import os
import json
import codecs

from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.utils.dateparse import parse_datetime
from django.db import IntegrityError
from django.shortcuts import render_to_response
from django.core.exceptions import ObjectDoesNotExist
from django.template.defaultfilters import slugify

from eventbrite import Eventbrite

# from home.models import Event
from events.models import Event
from .forms import BlogForm

# Create your views here.
def submit_blog(request, news_index):

      form = BlogForm(data=request.POST or None, label_suffix='')

      if request.method == 'POST' and form.is_valid():
          news_page = form.save(commit=False)
          news_page.slug = slugify(news_page.title)
          news = news_index.add_child(instance=news_page)
          if news:
              news.unpublish()
              # Submit page for moderation. This requires first saving a revision.
              news.save_revision(submitted_for_moderation=True)
              # Then send the notification to all Wagtail moderators.
              # send_notification(news.get_latest_revision().id, 'submitted', None)
          return HttpResponseRedirect(news_index.url)
      context = {
          'form': form,
          'news_index': news_index,
      }
      return render(request, 'blog_page_add.html', context)
