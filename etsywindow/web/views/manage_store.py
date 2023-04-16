from django.shortcuts import render, redirect

from ..models import Store, Listing

"""
The store listings now need to be created as a new section.
I want to get the listings layed out.

I need to click the trash can and have a confirmation pop up.
"""

def manage_store(request, store_id):
    if not request.user.is_authenticated:
        return redirect('login')
    
    store = Store.objects.filter(user_id=request.user, etsy_store_id=store_id).first()
    listings = Listing.objects.filter(store_id=store.id)

    if request.method == 'POST':
        if request.POST.get('action') == 'delete_store':
            context = {
                "store_id": store.id,
                "store_name": store.store_name,
                "store_url": store.store_url,
            }
            return render(request, 'confirm_delete_store.html', context=context)

        if request.POST.get('action') == 'confirm_delete_store':
            store.delete()
            return redirect('portal-home')

        if request.POST.get('action') == 'delete_listing':
            print("\n### Delete Listing ###")
            listing_id = request.POST.get('listing_id')
            listing_title = request.POST.get('listing_title')
            print("listing id:", listing_id)
            print("listing title:", listing_title)


    context = {
        'store': store,
        'listings': listings,
    }

    return render(request, 'manage_store.html', context=context)