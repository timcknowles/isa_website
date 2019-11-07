from __future__ import unicode_literals

from django import forms
from django.contrib.auth.forms import UserCreationForm, get_user_model
from registration.forms import RegistrationFormTermsOfService, RegistrationFormUniqueEmail
from django.utils.translation import ugettext_lazy as _

from wagtail.users.forms import UserEditForm, UserCreationForm
from news.models import NewsPage




class BlogForm(forms.ModelForm):
    class Meta:
        model = NewsPage
        labels = {
            'title': 'title',
            'intro': 'one line summary',
            'summary': 'summary',
            'first_name': 'first name',
            'last_name': 'last name',
            'email': 'email',
            'contact_number': 'contact number'


        }
        fields = [
            'title','intro', 'summary', 'first_name','last_name','email', 'contact_number'
        ]
    class Media:
        css =('all')
        js = ('all')
