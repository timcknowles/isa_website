

from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    modeladmin_register,
)
from .models import Event


class EventAdmin(ModelAdmin):
    """Event admin."""

    model = Event
    menu_label = "Events"
    menu_icon = "placeholder"
    menu_order = 290
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("title", "event_start", "api_url", "event_code", "venue_location" )
    search_fields = ("title", "event_start", "api_url",  "event_code", "venue_location" )
    inspect_view_enabled=True

modeladmin_register(EventAdmin)
