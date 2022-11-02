from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone

from apps.core.models import *
from PIL import Image

# Create your models here.


class Appointment(BaseModel):
    name = models.CharField(_("Name"), max_length=255)
    email = models.EmailField(_("Email"))
    phone = PhoneNumberField(_("Mobile No."), region="IN")  # as_e164

    PERSON_CHOICES = [
        (1, _("1 Person")),
        (2, _("2 Person")),
        (3, _("3 Person")),
        (4, _("4 Person")),
        (5, _("5 Person")),
        (6, _("6 Person")),
        (7, _("7 Person")),
    ]
    person = models.PositiveIntegerField(
        _("Person"), default=2, choices=PERSON_CHOICES)

    date = models.DateField(default=timezone.now)
    address = models.CharField(_("Address"), max_length=255)
    message = models.TextField(_("Message"), blank=True)


class Settings(SingletonModel):
    title = models.CharField(
        _("Site Title"), max_length=255, blank=True, default=_("Saloon"))

    icon = models.ImageField(
        _("Site Favicon"), upload_to="site_settings_icon_uploads/", help_text=_("Recommended Size: 96x96 Pixels"), blank=True)

    logo = models.ImageField(
        _("Site Logo"), upload_to="site_settings_logo_uploads/", help_text=_("Recommended Size: 150x90 Pixels"), blank=True)

    logo_white = models.ImageField(
        _("Site Logo White"), upload_to="site_settings_logo_uploads/", help_text=_("White color logo.Recommended Size: 150x90 Pixels"), blank=True)

    email = models.EmailField(
        _("E-Mail Address"), blank=True, default="contact@gmail.com")

    phone = models.CharField(_("Mobile No."), max_length=15, blank=True,
                             default="+91 99999 99999")  # as_e164

    address = models.TextField(
        _("Office Address"), blank=True, default=_("Our Address"))

    office_open = models.CharField(
        _("Office Open"), max_length=255, blank=True, default=_("Sun - Fri (08AM - 10PM)"))

    about_us = models.TextField(_("About Us Short Description"), blank=True, default=_(
        "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut tur incidunt ut labore et."))

    class Meta:
        verbose_name_plural = _("Settings")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        try:
            basewidth = 96
            model_image_path = self.icon.path
            img = Image.open(model_image_path)
            wpercent = basewidth / float(img.size[0])
            hsize = int((float(img.size[1]) * float(wpercent)))
            img.thumbnail((basewidth, hsize), Image.ANTIALIAS)
            img.save(model_image_path, "PNG")
        except Exception as ex:
            print("settings icon save error : ", ex)

        try:
            basewidth = 150
            model_image_path = self.logo.path
            img = Image.open(model_image_path)
            wpercent = basewidth / float(img.size[0])
            hsize = int((float(img.size[1]) * float(wpercent)))
            img.thumbnail((basewidth, hsize), Image.ANTIALIAS)
            img.save(model_image_path, "PNG")
        except Exception as ex:
            print("settings logo save error : ", ex)

        try:
            basewidth = 150
            model_image_path = self.logo_white.path
            img = Image.open(model_image_path)
            wpercent = basewidth / float(img.size[0])
            hsize = int((float(img.size[1]) * float(wpercent)))
            img.thumbnail((basewidth, hsize), Image.ANTIALIAS)
            img.save(model_image_path, "PNG")
        except Exception as ex:
            print("settings logo_white save error : ", ex)
