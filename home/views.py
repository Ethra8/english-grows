from django.shortcuts import render


def index(request):
    """ A view to return the index page """
    return render(request, 'home/index.html')


def companies(request):
    """ A view to return the companies page """
    return render(request, 'home/companies.html')

def company_services(request):
    """ A view to return the companies page """
    return render(request, 'home/companies.html')
