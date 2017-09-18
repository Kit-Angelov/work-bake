from django import template

register = template.Library()


@register.filter
def gramm(value):
    return int(float(value)*1000)
