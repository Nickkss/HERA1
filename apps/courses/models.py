from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator

from apps.core.models import *
from PIL import Image
import os

# Create your models here.


class Banner(SingletonModel):
    image = models.ImageField(
        upload_to="course_page_banner_uploads/",
        help_text=_(
            "Recommended Size: 1200x300 Pixels<br>Width: 1200px, Height: 300px"
        ),
    )
    alt_text = models.CharField(
        _("Alt Text"), max_length=255, blank=True, default="Banner"
    )

    class Meta:
        verbose_name_plural = _("Banner")


class Topic(BaseModel):
    title = models.CharField(_("Title"), max_length=255)
    course = models.ForeignKey(
        "Course",
        on_delete=models.CASCADE,
        related_name="topics",
        blank=True,
        help_text=_("Select course"),
    )

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ['created_on']


class Video(BaseModel):
    title = models.CharField(_("Video Title"), max_length=255, null=True)
    thumb = models.ImageField(
        _("Thumbnail Image"),
        upload_to="course_thumb_uploads/",
        blank=True,
        help_text=_("Upload thumbnail image if available."),
    )
    video = models.FileField(
        upload_to="course_video_uploads/", help_text=_("Upload course video.")
    )
    course = models.ForeignKey(
        "Course",
        on_delete=models.CASCADE,
        related_name="videos",
        blank=True,
        help_text=_("Select course"),
    )

    topic = models.ForeignKey(
        "Topic", on_delete=models.SET_NULL, null=True, blank=False, related_name="videos")

    def __str__(self):
        return str(self.title)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        try:
            basewidth = 720
            model_image_path = self.thumb.path
            img = Image.open(model_image_path)
            wpercent = basewidth / float(img.size[0])
            hsize = int((float(img.size[1]) * float(wpercent)))
            img.thumbnail((basewidth, hsize), Image.ANTIALIAS)
            img.save(model_image_path, "PNG")
        except Exception as ex:
            print("video thumb save error : ", ex)


class Course(SingletonModel):
    title = models.CharField(_("Course Title"), max_length=255)
    slug = models.SlugField(_("Slug"), unique=True,
                            help_text=_("autofill after save."))
    description = RichTextField(verbose_name=_("Description"), null=True)

    LEVEL_CHOICES = [(1, "Beginner Level"),
                     (2, "Medium Level"), (3, "Expert Level")]
    level = models.PositiveIntegerField(
        choices=LEVEL_CHOICES, default=1, blank=True)

    rating = models.FloatField(
        default=5, validators=[MinValueValidator(1), MaxValueValidator(5)], blank=True
    )
    STARS_CHOICES = [
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
        (5, "5"),
    ]

    # stars = models.PositiveIntegerField(choices=STARS_CHOICES, default=5)
    duration = models.CharField(
        _("Course Duration"),
        max_length=255,
        blank=True,
        default=_("4 Weeks"),
        help_text=_("Ex.: 4 Weeks"),
    )

    certificate = models.BooleanField(
        _("Completion Certificate"), default=True, blank=True
    )

    rewards = models.BooleanField(
        _("Enroll & Win Rewards"), default=True, blank=True)

    language = models.CharField(
        _("Language"), max_length=255, blank=True, default=_("English"))

    author = models.ForeignKey(
        "users.User", on_delete=models.SET_NULL, null=True, blank=True, related_name="course_added")

    def __str__(self):
        return str(self.title)

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.title)

        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("courses:Course")

    class Meta:
        verbose_name = _("Course")
        verbose_name_plural = _("Course")
