from django.shortcuts import render

# Create your views here.


def view_bag(request):
    """ Return a view of the shopping bag """

    return render(request, 'bag.html')
