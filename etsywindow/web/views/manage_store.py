from django.shortcuts import render, redirect

from ..models import Store, Listing


def manage_store(request, store_id):
    if not request.user.is_authenticated:
        return redirect('login')
    
    store = Store.objects.filter(user_id=request.user, etsy_store_id=store_id).first()
    listings = Listing.objects.filter(store_id=store.id)

    """
    The store listings now need to be created as a new section.
    I want to get the listings layed out.

    I need to click the trash can and have a confirmation pop up.
    """

    context = {
        'store': store
    }

    return render(request, 'manage_store.html', context=context)