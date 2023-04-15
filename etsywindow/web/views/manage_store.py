from django.shortcuts import render, redirect

from ..models import Store, Listing


def manage_store(request, store_id):
    if not request.user.is_authenticated:
        return redirect('login')
    
    store = Store.objects.filter(user_id=request.user, etsy_store_id=store_id).first()
    listings = Listing.objects.filter(store_id=store.id)
    print("\n### LISTINGS ###")
    for l in listings:
        print(l.id, l.image_url)


    context = {
        'store': store
    }

    return render(request, 'manage_store.html', context=context)