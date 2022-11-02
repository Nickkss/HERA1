from django.urls import path, include

urlpatterns = [
    path('', include("apps.users.urls")),
    path('', include("apps.courses.urls")),
    path('', include("apps.frontend.urls")),
]
