from django.shortcuts import render


from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages



def company_service(request):
    """ A view that renders the comany services page """

    return render(request, 'company_services/company_services.html')