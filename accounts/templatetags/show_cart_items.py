from django import template
from accounts.models import Cart


register = template.Library()
@register.inclusion_tag('cube/components/cart.html')
def show_cart_items(user):
    # user = context['request'].user
    cart = Cart.objects.get(user = user)
    cartItems = cart.cartitem_set.all()
    return {'cart' : cart, 'cartItems' : cartItems}