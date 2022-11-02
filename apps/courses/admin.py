from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from apps.core.admin import *
from .models import *

# Register your models here.


class VideoInline(admin.StackedInline):
    model = Video
    extra = 1


class BannerAdmin(BaseModelAdmin):
    list_display = ["id", "image", "updated_on",
                    "change_instance", "delete_instance"]


class VideoAdmin(BaseModelAdmin):
    list_display = [
        "title",
        "course",
        "change_instance",
        "delete_instance",
    ]
    search_fields = ["title", "course__title", "course__description"]
    list_filter = ["course", "created_on", "updated_on"]


class TopicInline(admin.StackedInline):
    model = Topic
    extra: int = 1


class CourseAdmin(BaseModelAdmin):
    def created_by(self, instance):
        if instance.author:
            return instance.author.name
        else:
            return "- - - - -"

    created_by.short_description = _("Created By")

    list_display = [
        "title",
        "slug",
        "created_by",
        "created_on",
        "updated_on",
        "change_instance",
        "delete_instance",
    ]
    search_fields = ("title", "slug", "description")
    list_filter = ["created_on", "updated_on"]

    prepopulated_fields = {"slug": ("title",)}
    inlines = [VideoInline, TopicInline]
    exclude = ('author',)
    readonly_fields = ('author',)

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)


admin.site.register(Banner, BannerAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Video, VideoAdmin)
