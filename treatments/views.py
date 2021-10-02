from django.shortcuts import render, get_object_or_404
from .models import Package


def all_treatments(request):
    """ A view to return the treatments package """

    treatments = Package.objects.all()

    context = {
        'treatments': treatments,
    }

    return render(request, 'treatments/treatments.html', context)


def package_detail(request, package_id):
    """ A view to sjow individual package """

    package = get_object_or_404(Package, pk=package_id)

    context = {
        'package': package,
    }

    return render(request, 'treatments/package_detail.html', context)
