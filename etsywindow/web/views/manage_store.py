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
    
    context = {}

    store = Store.objects.filter(user_id=request.user, etsy_store_id=store_id).first()
    if not store:
        return redirect('portal-home')

    listings = Listing.objects.filter(store_id=store.id)
    context = {
        'store': store,
        'listings': listings,
    }

    if request.method == 'POST':
        if request.POST.get('action') == 'delete_store':
            context = {
                "store_id": store.id,
                "store_name": store.store_name,
                "store_url": store.store_url,
            }
            return render(request, 'confirm_delete_store.html', context=context)

        if request.POST.get('action') == 'confirm_delete_store':
            if not store:
                return redirect('portal-home')

            store = Store.objects.filter(id=store.id).first()
            store.delete()
            return redirect('portal-home')

        if request.POST.get('action') == 'delete_listing':
            listing_id = request.POST.get('listing_id')
            listing = Listing.objects.filter(store_id=store.id, listing_id=listing_id).first()

            context['listing'] = {
                'listing_id': listing.id,
                'title': listing.title,
                'image_url': listing.image_url,
            }
            return render(request, 'confirm_delete_listing.html', context=context)

        if request.POST.get('action') == 'confirm_delete_listing':
            listing_id = request.POST.get('listing_id')
            listing = Listing.objects.filter(id=listing_id).first()

            if not listing:
                return redirect('manage-store', store_id=store_id)

            listing.delete()
            return redirect('manage-store', store_id=store_id)




    return render(request, 'manage_store.html', context=context)