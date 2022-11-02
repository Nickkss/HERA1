from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import View
from django.contrib import messages
from django.utils.translation import ugettext_lazy as _

from .models import Appointment
from .forms import AppointmentForm
# Create your views here.


class HomeView(View):
    def get(self, request):
        form = AppointmentForm()
        context = {"form": form}
        return render(request, "index.html", context=context)


class AboutView(View):
    def get(self, request):
        form = AppointmentForm()
        context = {"form": form}
        return render(request, "about.html", context=context)


class AppointmentView(View):
    def post(self, request):
        form = AppointmentForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _(
                "Thanks for appointment, your query has been submitted."))
        else:

            messages.error(request, _(f"Invalid Form: {form.errors}"))

        return redirect(request.META['HTTP_REFERER'])
