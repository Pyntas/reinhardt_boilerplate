# -*- coding: utf-8 -*-
from django import template
from django.conf import settings


register = template.Library()

@register.simple_tag()
def media(url):
    if settings.DEBUG:
        serving_url = settings.MEDIA_ROOT + url
    else:
        serving_url = settings.MEDIA_ROOT + url
    return serving_url


@register.simple_tag(takes_context=True)
def site_url(context):
    return settings.SITE_URL
