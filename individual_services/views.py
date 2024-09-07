from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import IndividualService

def individual_services(request):
    """ A view to return the individual services """

    services = IndividualService.objects.all()


    template = 'individual_services/individual_services.html'
    context = {
         'services': services,
    }
    return render(request, template, context)


