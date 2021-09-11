from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Hello World<h1>")
    return render(request, "home.html", {})


# def products_view(request, *args, **kwargs):
#    return render(request, "products.html", {})


def contacts_view(request, *args, **kwargs):
    return render(request, "contacts.html", {})
