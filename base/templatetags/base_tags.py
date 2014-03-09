#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.template import Library


register = Library()


@register.inclusion_tag('base/includes/analytics.html')
def analytics(unique_id, site_name):
    return {'unique_id': unique_id, 'site_name': site_name}


@register.simple_tag(takes_context=True)
def absolute_uri(context, path):
    return context['request'].build_absolute_uri(path)
