from django.contrib import admin
from wagtail.contrib.modeladmin.views import IndexView, WMABaseView
from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register
from feedback.models import Feedback


# Register your models here.
# class FeedbackAdminView(WMABaseView):
#     pass

# class FeedbackAdmin(ModelAdmin):
#     model = Feedback
#     index_view_class = FeedbackAdminView

# modeladmin_register(FeedbackAdmin) 