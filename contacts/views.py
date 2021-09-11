from django.shortcuts import render


# Create your views here.
def contacts_view(request, *args, **kwargs):
    return render(request, "contacts.html", {})
