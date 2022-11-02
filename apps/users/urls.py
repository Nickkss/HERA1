from django.urls import path

from .decorators import login_required
from . import views

app_name = "users"

urlpatterns = [
    path('login/', views.LoginView.as_view(), name="Login"),
    path('logout/', login_required(views.LogoutView.as_view()), name="Logout")
]
