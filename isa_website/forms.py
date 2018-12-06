from __future__ import unicode_literals

from django import forms
from django.contrib.auth.forms import UserCreationForm, get_user_model
from registration.forms import RegistrationFormTermsOfService, RegistrationFormUniqueEmail
from django.utils.translation import ugettext_lazy as _

from wagtail.users.forms import UserEditForm, UserCreationForm
# #
User = get_user_model()

class CustomForm(RegistrationFormTermsOfService, RegistrationFormUniqueEmail):
  first_name = forms.CharField(required=True, label=_('First Name'))
  last_name = forms.CharField(required=True, label=_('Last Name'))

  class Meta:
        model = User
        fields = ("username","email", "first_name", "last_name")

  # class Meta:
  #       model = User
  #       fields = (UsernameField(), "email","first_name")

  #
  # pass
