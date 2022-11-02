from django.contrib.auth import REDIRECT_FIELD_NAME
from django.shortcuts import render, resolve_url
from django.contrib import messages
from django.conf import settings
from django.urls import reverse
from django.shortcuts import redirect
from urllib.parse import urlparse

import uuid

home_url = "/"

def login_required(function=None, login_url=None, allowed_roles=None, redirect_field_name=REDIRECT_FIELD_NAME):
    def wrap(request, *args, **kwargs):
        # If the user is authenticated, return the view right away
        if request.user.is_authenticated:
            if allowed_roles!=None:
                if request.user.role in allowed_roles:
                    return function(request, *args, **kwargs)
                else:
                    messages.warning(request, "You are not authorized to visit this page.")
                    return redirect(home_url)
            return function(request, *args, **kwargs)

        # Otherwise, prepare login url (from django user_passes_test)
        # https://github.com/django/django/blob/master/django/contrib/auth/decorators.py#L10
        path = request.build_absolute_uri()
        resolved_login_url = resolve_url(login_url or settings.LOGIN_URL)
        login_scheme, login_netloc = urlparse(resolved_login_url)[:2]
        current_scheme, current_netloc = urlparse(path)[:2]
        if (not login_scheme or login_scheme == current_scheme) and (
            not login_netloc or login_netloc == current_netloc
        ):
            path = request.get_full_path()
        from django.contrib.auth.views import redirect_to_login

        return redirect_to_login(path, resolved_login_url, redirect_field_name)

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
