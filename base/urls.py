from django.contrib import admin
from django.urls import path, include
from django.urls import re_path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
    path("i18n/", include("django.conf.urls.i18n")),
    path('admin/', admin.site.urls),
    path('', include("apps.urls")),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
