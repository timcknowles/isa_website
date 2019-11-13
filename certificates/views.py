from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render
from certificates.forms import EmailForm
from certificates.models import Certificate

# from yourproject.utils import render_to_pdf  # created in step 4


# class GeneratePdf(View):
#     def get(self, request, *args, **kwargs):
#         data = {
#             "today": datetime.date.today(),
#             "amount": 39.99,
#             "customer_name": "Cooper Mann",
#             "order_id": 1233434,
#         }
#         pdf = render_to_pdf("pdf/invoice.html", data)
#         return HttpResponse(pdf, content_type="application/pdf")


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

    return render(request, "certificates.html", {"form": email, "attendance": attendence_record})
