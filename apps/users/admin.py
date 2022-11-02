from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.html import format_html
from django.db.models.query_utils import Q

from .models import *
from .forms import *

# Register your models here.


class CustomUserAdmin(UserAdmin):
    model = User

    list_display = (
        "email",
        "phone",
        "name",
        "id",
        "role",
        "is_active",
        "date_joined",
        "last_login",
    )
    list_filter = (
        "role",
        "is_staff",
        "is_active",
        "is_superuser",
        "date_joined",
        "last_login",
    )
    fieldsets = (
        ("Credentials", {"fields": ("email", "phone", "password", "role")}),
        ("Personal Info", {"fields": ("name",)}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (
            "Important Dates",
            {
                "fields": (
                    "date_joined",
                    "last_login",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "name",
                    "password1",
                    "password2",
                    "role",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
    )
    search_fields = ("email", "phone", "name", "id")
    ordering = ("date_joined", "is_superuser", "is_staff", "last_login")


admin.site.register(User, CustomUserAdmin)

# class Teacher(User):
#     class Meta:
#         proxy = True

# class TeacherAdmin(UserAdmin):
#     model = Teacher

#     list_display = ('email', 'phone', 'name', 'id',
#                     'role', 'is_active', 'date_joined', 'last_login')
#     list_filter = ('role', 'is_active', 'date_joined', 'last_login')
#     fieldsets = (
#         ("Credentials", {'fields': ('email', 'phone', 'password', 'role')}),
#         ('Personal Info', {'fields': ('name',)}),
#         ('Permissions', {'fields': ('is_active',)}),
#         ('Important Dates', {'fields': ('date_joined', 'last_login',)})
#     )
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('email', 'name', 'password1', 'password2', 'role', 'is_active')}
#          ),
#     )
#     search_fields = ('email', 'phone', 'name', 'id')
#     ordering = ('date_joined', 'is_superuser', 'is_staff', 'last_login')

#     def get_queryset(self, request):
#         return User.objects.filter(Q(role=2))

#     add_form = TeacherCreationForm

# admin.site.register(Teacher, TeacherAdmin)


class Student(User):
    class Meta:
        proxy = True


class StudentAdmin(UserAdmin):
    model = Student

    list_display = (
        "email",
        "phone",
        "name",
        "id",
        "role",
        "is_active",
        "date_joined",
        "last_login",
    )
    list_filter = ("role", "is_active", "date_joined", "last_login")
    fieldsets = (
        ("Credentials", {
         "fields": ("email", "phone", "password", "role", "is_active")}),
        ("Personal Info", {"fields": ("name",)}),
        ("Course", {"fields": ("course",)}),
        (
            "Important Dates",
            {
                "fields": (
                    "date_joined",
                    "last_login",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "name",
                    "password1",
                    "password2",
                    "role",
                    "is_active",
                ),
            },
        ),
    )
    search_fields = ("email", "phone", "name", "id")
    ordering = ("date_joined", "is_superuser", "is_staff", "last_login")

    def get_queryset(self, request):
        return User.objects.filter(Q(role=2))

    add_form = StudentCreationForm


admin.site.register(Student, StudentAdmin)
