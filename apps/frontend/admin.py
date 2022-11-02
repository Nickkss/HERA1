from django.contrib import admin

from apps.core.admin import BaseModelAdmin
from .models import *
# Register your model here.


@admin.register(Appointment)
class AppointmentAdmin(BaseModelAdmin):

    list_display = ['id', "name", "email", "phone", "person",
                    "created_on", "change_instance", "delete_instance"]


@admin.register(Settings)
class SettingsAdmin(BaseModelAdmin):
    list_display = ["title", "icon", "logo",
                    "email", "phone", "created_on", "updated_on"]
