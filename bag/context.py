from decimal import Decimal
from django.conf import settings


def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    pointless_number = Decimal(settings.A_NUMBER)

    context = {
        'pointless_number': pointless_number,
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
    }

    return context
