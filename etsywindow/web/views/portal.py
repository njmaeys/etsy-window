from django.shortcuts import render, redirect
from django.contrib import messages

from ..models import Store
from .utils.etsy_helper import get_shop_data


def portal_home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    context = {
        'has_store': False,
        'store': None,
    }
    
    stores = Store.objects.filter(user_id=request.user)
    if not stores:
        # Show the add store form
        if request.method == 'POST':
            if request.POST.get('action') == 'add_store':
                # Lookup the store data from Etsy
                store_name = request.POST.get('store-name', None)
                store_data = get_shop_data(store_name=store_name)
                store_data = store_data['results'][0]

                store_id = store_data['shop_id']
                store_name = store_data['shop_name']
                store_url = store_data['url']

                if not store_name:
                    messages.error(request, "Store not found.")
                    return redirect('portal-home')
                
                ## Create the store object
                #Store.objects.create(
                #    user_id_id=request.user.id,
                #    store_name=store_name,
                #    etsy_store_id=store_id,
                #)

                """
                TODO: Start back here and add in the confirmation template of the data
                """


                messages.success(request, "Store created successfully!")
                return redirect('portal-home')
        else:
            return render(request, 'portal_home.html', context)
    
    context['has_store'] = True
    context['store'] = stores[0]

    return render(request, 'portal_home.html', context)
    