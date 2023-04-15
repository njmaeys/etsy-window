from django.shortcuts import render, redirect

from ..models import Store
from .utils.etsy_helper import get_shop_data


def portal_home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    context = {
        'has_store': False,
    }

    stores = Store.objects.filter(user_id=request.user)
    if not stores:
        if request.method == 'POST' and request.POST.get('action') == 'add_store':
            store_name = request.POST.get('store-name')
            store_data = get_shop_data(store_name=store_name)

            store_data = store_data.get('results', None)
            if not store_data:
                context['message'] = 'The store you entered does not exist.'
                return render(request, 'portal_home.html', context=context)
            
            store = store_data[0]
            context['store_id'] = store['shop_id']
            context['store_name'] = store['shop_name']
            context['store_url'] = store['url']

            return render(request, 'confirm_store.html', context=context)
        elif request.method == 'POST' and request.POST.get('action') == 'confirm_store':
            Store.objects.create(
                user_id=request.user,
                etsy_store_id=request.POST.get('store_id'),
                store_name=request.POST.get('store_name'),
                store_url=request.POST.get('store_url')
            )
            return redirect('portal-home')
        else:
            return render(request, 'portal_home.html', context=context)
    else:
        context['stores'] = stores
        context['has_store'] = True

        return render(request, 'portal_home.html', context=context)

    