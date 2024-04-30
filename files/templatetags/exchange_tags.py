from django import template
from files.models import *

register = template.Library()

@register.simple_tag(name='getgenres')
def get_genres(filter=None):
    if not filter:
        return Genre.objects.all()
    else:
        return Genre.objects.filter(pk=filter)

@register.inclusion_tag('files/list_genres.html')
def show_genres(sort=None):
    if not sort:
        genres = Genre.objects.all()
    else:
        genres = Genre.objects.order_by(sort)

    return {"genres": genres}