from django.shortcuts import render


def shop(request):
    """ A view to return the classes """

    return render(request, 'shop/shop.html')