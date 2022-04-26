from django import template

register = template.Library()

@register.filter
def getType(value) :
    return type(value).__name__
