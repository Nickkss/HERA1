from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.db.models.query_utils import Q
from django.urls import reverse
from django.contrib.sessions.models import Session
from django.conf import settings


from PIL import Image
import os
import random
import string

# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self, name, email, password, **extra_fields):
        if not name:
            raise ValueError(_("The Name must be set"))

        if not email:
            raise ValueError(_("The Email must be set"))

        email = self.normalize_email(email)
        user = self.model(name=name, email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, name, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))

        return self.create_user(name, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    id = models.BigAutoField(unique=True, primary_key=True, editable=False)
    username = None
    name = models.CharField(_("Name"), max_length=255)
    email = models.EmailField(_("E-Mail Address"), unique=True, null=True)
    phone = PhoneNumberField(_("Mobile No."), blank=True)  # as_e164

    ROLE_CHOICES = [
        (1, "Admin"),
        # (2, "Teacher"),
        (2, "Student"),
    ]
    role = models.SmallIntegerField(
        _("Role"), choices=ROLE_CHOICES, default=2, help_text=_("Choose User Role")
    )

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(default=timezone.now)

    # Student Part
    course = models.ForeignKey(
        "courses.Course", on_delete=models.SET_NULL, related_name="students", blank=True, null=True
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    objects = UserManager()

    def __str__(self):
        return str(self.name).capitalize()

    def save(self, *args, **kwargs):
        if self.role == 1:
            self.is_superuser = True
            self.is_staff = True
            self.is_active = True

        if self.is_superuser:
            self.role = 1

        super().save(*args, **kwargs)

    def get_admin_url(self):
        info = (self._meta.app_label, self._meta.model_name)
        return reverse("admin:%s_%s_change" % info, args=(self.pk,))

    def get_logout_url(self):
        return reverse("users:Logout")

    @property
    def get_courses(self):

        courses = self.courses.all().filter(Q(publish=True))
        return courses

    class Meta:
        ordering = ["-last_login"]


class UserSession(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    session = models.OneToOneField(Session, on_delete=models.CASCADE)
