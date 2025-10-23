from .models import Cart, CartItem


def cart(request):
    """Add cart information to template context"""
    cart_items = []
    cart_total = 0
    cart_count = 0

    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_items = cart.items.all()
        cart_total = cart.get_total_price()
        cart_count = cart.get_total_items()
    else:
        # For anonymous users, use session-based cart
        session_key = request.session.session_key
        if session_key:
            cart, created = Cart.objects.get_or_create(session_key=session_key)
            cart_items = cart.items.all()
            cart_total = cart.get_total_price()
            cart_count = cart.get_total_items()

    return {
        'cart_items': cart_items,
        'cart_total': cart_total,
        'cart_count': cart_count,
    }
