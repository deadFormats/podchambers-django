from django import template
from django.template.loader import get_template


register = template.Library()


@register.inclusion_tag('default.html', takes_context=True)
def in_dev_template(**kwargs):
    return kwargs


@register.filter
def add_class_to_field(field, class_name):
    if len(field.errors) > 0:
        class_name += ' is-danger'
    field_classes = field.field.widget.attrs.get('class', '')
    field_classes += f' {class_name}'
    return field.as_widget(attrs={'class': field_classes})
