""" Items imported from Django """
from django.shortcuts import render, get_object_or_404
from .models import Product


def products_view(request):
    """ A view to show all products """
    from_database = Product.objects.all()

#    if request.POST:
#       sort_type = request.GET['sort_type']
#       print(sort_type)
#       return

    from_database = from_database.order_by('title')

    my_context = {
        'from_database': from_database,
    }

    # products = Product.objects.all()

    return render(request, "products.html", my_context)


def product_detail(request, product_id):
    """ A view to show product detail """
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    # products = Product.objects.all()

    return render(request, "product_detail.html", context)
