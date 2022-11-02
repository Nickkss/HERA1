from django import template
from django.urls import reverse

register = template.Library()


@register.filter(name="range")
def range_filter(a, b=None):
    a = int(a)
    if b is not None:
        b = int(b)
        return range(a, b)
    else:
        return range(a)
