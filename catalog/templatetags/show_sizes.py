from django import template
from catalog.models import Size
register = template.Library()
@register.inclusion_tag('cube/shop/components/size-list.html')
def show_sizes():
    sizes = Size.objects.all()
    return {'sizes' : sizes}