from django import template
from accounts.models import Cart


register = template.Library()
@register.inclusion_tag('cube/account/components/side-cart-items.html')
def show_cart_items(user):
    cart, _ = Cart.objects.get_or_create(user = user)
    cartItems = cart.cartitem_set.all()
    return {'cart' : cart, 'cartItems' : cartItems}