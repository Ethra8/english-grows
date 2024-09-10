from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from individual_services.models import IndivService



# Create your views here.

def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """
    service = get_object_or_404(IndivService, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
        messages.success(request, f'Updated {service.name} to {bag[item_id]}')
    else:
        bag[item_id] = quantity
        messages.success(request, f'Added {service.name} to your bag')

    request.session['bag'] = bag
    
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""
    service = get_object_or_404(IndivService, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})


    if quantity >= 1:
        bag[item_id] = quantity
    else:
        bag.pop(item_id)
        messages.success(request, f'Removed {product.name} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('bag'))


def remove_bag_item(request, item_id):
    """Remove the item from the shopping bag"""
    try:
        service = get_object_or_404(IndivService, pk=item_id)
        bag = request.session.get('bag', {})

        # Remove the item from the bag
        bag.pop(item_id)  # Use .pop() with a default to avoid KeyError if item_id is not found
        messages.success(request, f'Removed {service.name} from your bag')

        # Update the session
        request.session['bag'] = bag

        return HttpResponse(status=200)  # Return success status

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)  # Return error status