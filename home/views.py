from django.shortcuts import render

# Create your views here.

def index(request):
    """ A view to return the index page """
    return render(request, 'home/index.html')


def companies(request):
    """ A view to return the companies page """
    return render(request, 'home/companies.html')
