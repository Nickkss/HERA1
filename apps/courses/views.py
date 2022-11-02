from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from django.views.generic import View, DetailView
from django.urls import reverse
from django.db.models.query_utils import Q
from django.contrib import messages

from .models import *

# Create your views here.


class ListCoursesView(View):
    def get(self, request):
        q = request.GET.get("q", "").strip()
        courses = Course.objects.filter(Q(publish=True))
        if q:
            courses = courses.filter(
                Q(title__icontains=q) | Q(description__icontains=q)
            )
        else:
            q = None
        context = {"objects": courses, "search_query": q}
        return render(request, "courses/list_courses.html", context=context)


class CourseView(View):
    def get(self, request):
        course = Course.load()
        topics = Topic.objects.all()
        context = {'course': course, 'topics': topics}
        return render(request, "courses/course.html", context=context)


class CourseDetailView(View):
    def get(self, request, slug):
        # Course.objects.filter(Q(publish=True))
        course = get_object_or_404(Course, slug=slug)
        if course not in request.user.courses.all():
            messages.warning(
                request, "This course is not added to your profile yet.")
            return redirect(reverse("courses:Courses"))

        context = {"course": course}
        response = render(request, "courses/course.html", context=context)
        # response['X-Frame-Options'] = 'SAMEORIGIN'
        return response
