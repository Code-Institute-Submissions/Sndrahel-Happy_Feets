from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category, Review
from .forms import ProductForm, ReviewForm

# pylint: disable=no-member


def shop_products(request):
    """ A view to return the shop products """

    shop = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                shop = shop.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            shop = shop.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            shop = shop.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "Sorry, you didn't enter any search criteria!")
                return redirect(reverse('shop'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            shop = shop.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'shop': shop,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'shop/shop.html', context)


def product_detail(request, product_id):
    """ A view to show individual shop products """

    product = get_object_or_404(Product, pk=product_id)

    # Reviews code adapted from:
    # https://github.com/johnvenkiah/CI_PP5_John_Venkiah/blob/main/products/views.py)

    reviews = Review.objects.filter(product=product)

    if request.method == 'POST':

        review_form = ReviewForm(data=request.POST or None)

        if request.user.is_authenticated and review_form.is_valid():
            review_form.instance.user = request.user
            review = review_form.save(commit=False)
            review.product = product
            review.save()
            messages.success(
                request, (
                    f'Thank you for reviewing "{product.name[:25]}.."! '
                    'You can now view and remove it below.'
                )
            )

            if product.rating:
                product.rating = (product.rating + review.product_rating) / 2
            else:
                product.rating = review.product_rating
            product.save()

            return redirect(reverse('product_detail', args=[product.id]))
    else:
        review_form = ReviewForm()

    context = {
        'product': product,
        'reviews': reviews,
        'review_form': review_form,
    }

    return render(request, 'shop/product_detail.html', context)


@login_required
def add_product(request):
    """ Add new products """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Product was successfully added')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. \
                Please check the form is valid.')
    else:
        form = ProductForm()

    template = 'shop/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit an existing product """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product successfully updated')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. \
                Please check the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'shop/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete an existing product """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('shop'))
