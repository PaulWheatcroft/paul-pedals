""" Items imported from Django """
from django.shortcuts import render, get_object_or_404
from .models import Product


def products_view(request):
    """ A view to show all products """
    from_database = Product.objects.all()

    sort_type = request.POST.get('sort-selector')
    print(sort_type)
    if sort_type is None:
        from_database = from_database.order_by('title')
        my_context = {
            'from_database': from_database,
            'sort_type': sort_type,
        }
        return render(request, "products.html", my_context)
    if sort_type == 'name_asc':
        from_database = from_database.order_by('title')
        my_context = {
            'from_database': from_database,
            'sort_type': sort_type,
        }
        return render(request, "products.html", my_context)
    if sort_type == 'name_desc':
        from_database = from_database.order_by('-title')
        my_context = {
            'from_database': from_database,
            'sort_type': sort_type,
        }
        return render(request, "products.html", my_context)
    if sort_type == 'price_asc':
        from_database = from_database.order_by('price')
        my_context = {
            'from_database': from_database,
            'sort_type': sort_type,
        }
        return render(request, "products.html", my_context)
    if sort_type == 'price_desc':
        from_database = from_database.order_by('-price')
        my_context = {
            'from_database': from_database,
            'sort_type': sort_type,
        }
        return render(request, "products.html", my_context)


def product_detail(request, product_id):
    """ A view to show product detail """
    product = get_object_or_404(Product, pk=product_id)
    print(request.path)
    context = {
        'product': product,
    }

    # products = Product.objects.all()

    return render(request, "product_detail.html", context)
