from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.db.models.query_utils import Q
from django.views.generic import View
from django.contrib import messages

from django.contrib.auth import user_logged_in
from django.dispatch.dispatcher import receiver
from django.contrib.sessions.models import Session

from .models import *


# Create your views here.
@receiver(user_logged_in)
def remove_other_sessions(sender, user, request, **kwargs):
    if not user.is_superuser:
        if user.role == 1:
            head = user.head
            school = head.school
            if not school:
                schools = user.get_own_schools
                head.school = schools.first()
                head.save()

        # remove other sessions
        Session.objects.filter(usersession__user=user).delete()

        # save current session
        request.session.save()

        # create a link from the user to the current session (for later removal)
        UserSession.objects.get_or_create(
            user=user,
            session_id=request.session.session_key
        )
    else:
        pass


class LoginView(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect(reverse("courses:Course"))
        form = AuthenticationForm(request)
        context = {'form': form}
        return render(request, "auth/login.html", context=context)

    def post(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            user.last_login = timezone.now()
            user.save()
            login(request, user)
            messages.success(request, "Login Success !")
            next = self.request.GET.get("next", None)
            if next:
                return redirect(next)
            else:
                return redirect(reverse("courses:Course"))
        else:
            messages.error(request, "User not found!")
        return redirect(reverse("users:Login")+"#login")


class LogoutView(View):
    def get(self, request):
        logout(request)
        messages.info(request, "Logged Out !")
        return redirect(reverse("frontend:Home"))
