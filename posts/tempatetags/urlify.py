from urllib import quote_plus
from django import template

register = template.Library()

assert isinstance(register.filter, object)


@register.filter
def urlify(value):
    return quote_plus(value)
