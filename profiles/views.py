from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import UserProfile
from .forms import UserProfileForm

from checkout.models import Order

@login_required
def profile(request):
    """ Display the user profile """
    profile = get_object_or_404(UserProfile, user=request.user)
    orders = Order.objects.filter(user_profile=profile).order_by('-date')  # Use user_profile here
    
    # Update user profile info via POST in form
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully')
        else:
            messages.error(request, 'Update failed. Please ensure the form is valid.')
    else:
        form = UserProfileForm(instance=profile)

    orders = orders.order_by('-date')

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'profile': profile,
    }

    return render(request, template, context)


    @receiver(post_save, sender=User)
    def create_or_update_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)
        else:
            instance.userprofile.save()



def order_history(request, order_number):
    '''
    Display one single order's detail once
    user clicks on an order on profile.
    '''
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (f'This is a past confirmation for order {order_number}\
        A confirmation email was sent on the order date'))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)