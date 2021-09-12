from django.shortcuts import render
from .models import Product


def products_view(request):
    from_database = Product.objects.all()

    my_context = {
        "the_text": "these are words",
        'the_number': 123,
        'the_boolean': True,
        'from_database': from_database,
    }

    # products = Product.objects.all()

    return render(request, "products.html", my_context)
