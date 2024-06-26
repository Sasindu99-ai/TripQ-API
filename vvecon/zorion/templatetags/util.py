import json

from django import template
from django.core.serializers import serialize
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter
@stringfilter
def split(value, delimiter):
    return value.split(delimiter)


@register.filter
def jsonify(queryset):
    return json.loads(serialize('json', queryset))
