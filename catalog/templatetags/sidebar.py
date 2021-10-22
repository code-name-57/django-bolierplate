from django import template
from catalog.models import Collection, Size
register = template.Library()
@register.inclusion_tag('cube/shop/components/sidebar.html')
def sidebar():
    collections = Collection.objects.all()
    sizes = Size.objects.all()

    return {'collections' : collections, 'sizes': sizes}