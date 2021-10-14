from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Package, Category
from .forms import PackageForm


def all_treatments(request):
    """ A view to return the treatments package """

    treatments = Package.objects.all()
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
                treatments = treatments.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            treatments = treatments.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            treatments = treatments.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        """ View to filter packages through search bar """
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(
                    request, "Sorry, you didn't enter any search criteria!")
                return redirect(reverse('treatments'))

            queries = Q(name__icontains=query) | Q(
                description__icontains=query)
            treatments = treatments.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'treatments': treatments,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'treatments/treatments.html', context)


def package_detail(request, package_id):
    """ A view to show individual package """

    package = get_object_or_404(Package, pk=package_id)

    context = {
        'package': package,
    }

    return render(request, 'treatments/package_detail.html', context)


def add_package(request):
    """ Add a package to the store """
    form = PackageForm()
    template = 'treatments/add_package.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


