from django import template
from django.template.loader import get_template


register = template.Library()


@register.inclusion_tag('default.html', takes_context=True)
def in_dev_template(**kwargs):
    return kwargs
