from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render
from certificates.forms import EmailForm
from certificates.models import Certificate



def ViewAttendance(request):
    # view to eneter email and see attendances

    if request.method == "POST":
        # if we've submitted an email address
        email = EmailForm(request.POST)
        if email.is_valid():
            # make a database query and return the data
            attendence_record = Certificate.objects.filter(
                email_address=email.cleaned_data["email"]
            ).order_by('event_id_id')

    else:
        email = EmailForm()
        attendence_record = {}

    return render(request, "certificates.html", {"form": email, "attendance": attendence_record})
