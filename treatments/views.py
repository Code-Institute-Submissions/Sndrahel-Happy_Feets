from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Package, Category


def all_treatments(request):
    """ A view to return the treatments package """

    treatments = Package.objects.all()
    query = None
    categories = None

    if request.GET:
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

    context = {
        'treatments': treatments,
        'search_term': query,
        'current_categories': categories,
    }

    return render(request, 'treatments/treatments.html', context)


def package_detail(request, package_id):
    """ A view to sjow individual package """

    package = get_object_or_404(Package, pk=package_id)

    context = {
        'package': package,
    }

    return render(request, 'treatments/package_detail.html', context)
