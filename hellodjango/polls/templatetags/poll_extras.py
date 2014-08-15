from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def echo(value):
    text = '<ul>'
    for v in value:
        text += '<li>{0}</li>'.format(v.question)
    text += '</ul>'
    return mark_safe(text)
