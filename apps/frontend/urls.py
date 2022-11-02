from django.urls import path

from . import views

app_name = "frontend"

urlpatterns = [
    path('', views.HomeView.as_view(), name="Home"),
    path('about-us/', views.AboutView.as_view(), name="About"),
    path("appointment/", views.AppointmentView.as_view(), name="Appointment"),
]
