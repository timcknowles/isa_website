import os
import tweepy

from django.http import HttpResponse
from wagtail.core import hooks

#get the tokens
consumer_token = os.environ.get('CONSUMER_KEY')
consumer_secret = os.environ.get('CONSUMER_SECRET')
access_token = os.environ.get('ACCESS_TOKEN')
access_token_secret = os.environ.get('ACCESS_TOKEN_SECRET')


@hooks.register('after_create_page')
def do_after_page_create(request, Page):

    #Have some kind of if page.tweet=TRue statement


    #setup the authentication
    auth = tweepy.OAuthHandler(consumer_token, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    post_url = "http://isawebsite.com" + Page.url_path
    isa_tweet = "New post: \n" + Page.title + "\n " + post_url

    #tweet!
    api.update_status(isa_tweet)
    print('\n url: ', Page.full_url, '\n title: ', Page.title, '\n relative url:', Page.relative_url, '\n url path:', Page.url_path)
    return HttpResponse("Congrats on making an event", content_type="text/plain")
