from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse

# Register your models here.


class BaseModelAdmin(admin.ModelAdmin):
    def delete_instance(self, obj):
        info = obj._meta.app_label, obj._meta.model_name
        url = reverse("admin:%s_%s_delete" % info, args=(obj.id,))
        delete_button = f"""<a href="{url}" class="btn btn-danger"><i class="fas fa-trash"></i></a>"""
        return format_html(delete_button)

    delete_instance.allow_tags = True
    delete_instance.short_description = "Delete"

    def change_instance(self, obj):
        info = obj._meta.app_label, obj._meta.model_name
        url = reverse("admin:%s_%s_change" % info, args=(obj.id,))
        change_button = f"""<a href="{url}" class="btn btn-primary"><i class="fas fa-pencil-alt"></i></a>"""
        return format_html(change_button)

    change_instance.allow_tags = True
    change_instance.short_description = "Edit"
