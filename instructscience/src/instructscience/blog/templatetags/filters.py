from django import template


register = template.Library()


@register.filter
def featured(value, args):
    return value.filter(featured=args)

@register.filter
def tens(value):
    return value*10


@register.filter
def minus(value):
    return value

@register.filter
def minusone(value):
    return value-1
