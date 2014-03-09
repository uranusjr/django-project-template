#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.utils.html import format_html
from django.utils.translation import ugettext_lazy as _


def view_in_site(obj):
    return format_html(
        '<a href="{url}" target="_blank">{text}</a>',
        url=obj.get_absolute_url(),
        text=view_in_site.short_description,
    )

view_in_site.short_description = _('View in site')
