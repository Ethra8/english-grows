from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from .models import IndivService, IndividualType


def individual_services(request):
    """A view to return the list of individual services with sorting and filtering"""
    
    services = IndivService.objects.all()  # Get all individual services
    categories = IndividualType.objects.all()  # Get all individual service types
    query = None
    category_filter = None
    sort = None
    direction = None

    # Check if any GET parameters were passed for sorting/filtering
    if request.GET:
        # Sorting
        if 'sort' in request.GET:
            sort = request.GET['sort']
            if sort == 'name':
                services = services.order_by('name')
            elif sort == 'price':
                services = services.order_by('price')

        # Sorting direction
        if 'direction' in request.GET:
            direction = request.GET['direction']
            if direction == 'desc':
                services = services.reverse()  # Reverse the sorted queryset

        # Search functionality
        if 'q' in request.GET:
            query = request.GET['q']
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            services = services.filter(queries)

    current_sorting = f'{sort}_{direction}'  # Keep track of current sorting

    # Context to pass to the template
    context = {
        'services': services,
        'search_term': query,
        'current_category': category_filter,
        'current_sorting': current_sorting,
    }

    return render(request, 'individual_services/individual_services.html', context)


def pack_details(request, service_id):
    """ A view to return the pack details page """
    service = get_object_or_404(IndivService, pk=service_id)

    context = {
        'service': service,
    }

    return render(request, 'individual_services/pack_details.html', context)