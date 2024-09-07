from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.db.models import Q
from django.db.models.functions import Lower

from .models import IndivService, IndividualType


def individual_services(request):
     """ A view to return the individual services """
     services = IndivService.objects.all()
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

     if 'type' in request.GET:
          types = request.GET['type'].split(',')
          services = services.filter(type__name__in=types)
          types = IndividualType.objects.filter(name__in=types)
          if 'q' in request.GET:
               query = request.GET['q']
               if not query:
                    messages.error(request, "You didn't enter any search criteria!")
                    return redirect(reverse('services'))

          queries = Q(name__icontains=query) | Q(description__icontains=query) # ! the '|' is= OR, avoiding django logic which would need to find the query BOTH in name & description.
          services = services.filter(queries)

     current_sorting = f'{sort}_{direction}'

     print(current_sorting)
     print(types)

     template = 'individual_services/individual_services.html'

     context = {
         'services': services,
         'search_term': query,
         'current_types': types,
         'current_sorting': current_sorting,
     }
     return render(request, template, context)


