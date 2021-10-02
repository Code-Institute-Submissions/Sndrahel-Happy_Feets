from django.shortcuts import render
from .models import Package


def all_treatments(request):
    """ A view to return the treatments package """

    treatments = Package.objects.all()

    context = {
        'treatments': treatments,
    }

    return render(request, 'treatments/treatments.html', context)
