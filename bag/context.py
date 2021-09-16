from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    pointless_number = Decimal(settings.A_NUMBER)
    bag = request.session.get('bag', {})

    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        line_price = product.price * quantity
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
            'line_price': line_price
        })

    context = {
        'pointless_number': pointless_number,
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
    }

    return context
