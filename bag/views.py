from django.shortcuts import render, redirect

# Create your views here.


def view_bag(request):
    """ Return a view of the shopping bag """

    return render(request, 'bag.html')


def add_to_bag(request, item_id):
    """ View to add items to a bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    print('add_to_bag')
    print(request.session['bag'])
    return redirect(redirect_url)


def amend_to_bag(request, item_id):
    """ View to add items to a bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag')

    bag[item_id] = quantity

    request.session['bag'] = bag
    print('amend_to_bag')
    print(request.session['bag'])
    return redirect(redirect_url)


def remove_bag_item(request, item_id):
    """ View to add items to a bag """

    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})
    item_number = item_id

    del bag[item_number]

    request.session['bag'] = bag

    print('remove_bag_item')
    print(bag)
    print(item_number)
    return redirect(redirect_url)
