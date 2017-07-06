"""
Usage: put {% load humanification %} in the template where you
want to use any of these additional template tags
"""
import random

from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag()
def random_human_image(size):
    HUMANS = ['arnoud', 'jeffry', 'kelly', 'marino', 'nick', 'paul', 'stanley', 'yuri']
    name = random.choice(HUMANS)
    return '//cdn.cyso.nl/fuga/img/humans/{size}/{name}.png'.format(size=size, name=name)
