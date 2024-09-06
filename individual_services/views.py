from django.shortcuts import render


def individual_services(request):
    """ A view to return the individual services """
    template = 'individual_services/individual_services.html'
    context = {
        
    }
    return render(request, template, context )


