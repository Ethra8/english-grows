from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from .models import IndivService, IndividualType


def individual_services(request):
    """ A view to return the individual services """
    services = IndivService.objects.all()
    print(services)

    # for s in services:
    #     get_indivservice_type()

    # service_type = [(s.id, s.get_indivservice_type()) for s in services]
    # print(f'This is var service_type: {service_type}')

    # to avoid errors when loading individual_services page if there is no value on GET yet, set all GET vars to None:
    query = None
    types = None
    sort = None
    direction = None

    # if form included in search items box is activated through GET
    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey

            if sortkey == 'name':
                sortkey = 'lower_name'
                services = services.annotate(lower_name=Lower('name'))

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            
            services = services.order_by(sortkey)
            print(services)

            if 'type' in request.GET:
                types = request.GET['type']
                services = services.filter(type__name__in=types)
                categories = IndividualType.objects.filter(name__in=types)

            if 'q' in request.GET:
                query = request.GET['q']
                queries = Q(type__icontains=query) | Q(description__icontains=query)
                services = services.filter(queries)
                
                # services = services.filter(types)   type=individuals_private

    current_sorting = f'{sort}_{direction}'

    template = 'individual_services/individual_services.html'

    context = {
        'services': services,
        'search_term': query,
        'current_types': types,
        'current_sorting': current_sorting,
    }

    return render(request, template, context)


