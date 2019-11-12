from django.shortcuts import render
from feedback.forms import FeedbackForm


# Create your views here.
def give_feedback(request):
    form = FeedbackForm()

    return render(request, 'feedback.html', {'form':form})