from django.shortcuts import render, redirect
from feedback.forms import FeedbackForm
from feedback.models import Feedback

# Create your views here.
def give_feedback(request, event):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(f'/view_feedback/{event}')
        else:
            print("form not valid")
    else:
        form = FeedbackForm(initial={'eventid':event})
        return render(request, 'feedback.html', {'form':form, 'event':event})

def ViewEventFeedback(request, event):
    event_feedback = Feedback.objects.filter(eventid = event)
    print(event_feedback)
    for i in event_feedback:
        k = vars(i)
        for j in range(6):
            print(f'useful_{j}')
            print(k[f'useful_{j}'])
    return render(request, 'view_event_feedback.html', {"events": event_feedback})