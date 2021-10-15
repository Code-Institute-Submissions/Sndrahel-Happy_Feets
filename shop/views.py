from django.shortcuts import render
from .models import Product


def shop_products(request):
    """ A view to return the products """

    shop = Product.objects.all()

    context = {
        'shop': shop,
    }

    return render(request, 'shop/shop.html', context)


def product_detail(request, product_id):
    """ A view to show individual shop products """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'shop/product_detail.html', context)
