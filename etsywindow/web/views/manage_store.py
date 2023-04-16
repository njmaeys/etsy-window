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

    print("\n### HERE ###")
    if request.method == 'POST':
        if request.POST.get('action') == 'delete_store':
            print("\n### DELETE STORE ###")
            print("store id:", store.id)
            print("etsy store id:", store.etsy_store_id)


    context = {
        'store': store
    }

    return render(request, 'manage_store.html', context=context)