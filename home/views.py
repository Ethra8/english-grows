from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from .models import CompanyContact
from .forms import CompanyContactForm


def index(request):
    """ A view to return the index page """
    return render(request, 'home/index.html')


def companies(request):
    """ A view to return the companies page with form"""

    form = CompanyContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Your message has been sent successfully!')
        return redirect('companies')
    form = CompanyContactForm()

    return render(request, 'home/companies.html', {'form': form})