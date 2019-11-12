from django.forms import ModelForm, RadioSelect
from feedback.models import Feedback

class FeedbackForm(ModelForm):
    class Meta:
        model = Feedback
        fields = '__all__'
        # widgets = {
        #     "useful_1": RadioSelect
        # }
