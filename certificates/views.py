from django.http import HttpResponse
from django.views.generic import View

from yourproject.utils import render_to_pdf #created in step 4

class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        data = {
             'today': datetime.date.today(),
             'amount': 39.99,
            'customer_name': 'Cooper Mann',
            'order_id': 1233434,
        }
        pdf = render_to_pdf('pdf/invoice.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
