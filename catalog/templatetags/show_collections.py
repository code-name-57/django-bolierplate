from django import template
from catalog.models import Collection
register = template.Library()
@register.inclusion_tag('cube/shop/components/collection-list.html')
def show_collections():
    collections = Collection.objects.all()
    return {'collections' : collections}