from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    modeladmin_register,
)
from .models import Certificate


class CertificateAdmin(ModelAdmin):
    """Subscriber admin."""

    model = Certificate
    menu_label = "Certificates"
    menu_icon = "placeholder"
    menu_order = 290
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("attendee_name", "email_address", "attended", "feedback_complete", "event_id")
    # search_fields = ("email", "full_name",)



modeladmin_register(CertificateAdmin)
