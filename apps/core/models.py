from django.db import models
from django.utils.translation import gettext_lazy as _
import string
import random

# Create your models here.

ID_MAX_LENGTH = 8


class BaseModel(models.Model):
    id = models.CharField(
        _("ID"),
        max_length=ID_MAX_LENGTH,
        unique=True,
        primary_key=True,
        blank=True,
        editable=False,
        help_text=_("Automatically Set After Save"),
    )
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    updated_on = models.DateTimeField(auto_now=True, null=True)

    def save(self, *args, **kwargs):
        # Child Model = self._meta.model
        # Generate Random ID
        if not self.id:
            self.id = "".join(
                random.choices(string.ascii_uppercase +
                               string.digits, k=ID_MAX_LENGTH)
            )

        super(BaseModel, self).save(*args, **kwargs)

    class Meta:
        abstract = True


class SingletonModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    updated_on = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj
