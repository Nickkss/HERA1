from django.urls import path

from . import views
from apps.users.decorators import login_required

app_name = "courses"

urlpatterns = [
    # path("courses/", views.ListCoursesView.as_view(), name="Courses"),
    # path("course/<slug>/", login_required(views.CourseDetailView.as_view(),
    #      allowed_roles=[1, 2]), name="Course"),

    path("course/", login_required(views.CourseView.as_view(),
         allowed_roles=[1, 2]), name="Course")
]
