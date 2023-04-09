from django.shortcuts import render, redirect
from django.contrib import messages

from ..models import Store


def portal_home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    if request.method == 'POST':
        if request.POST.get('action') == 'add_store':
            # Create the store object
            store_name = request.POST.get('store-name', None)
            store_id = request.POST.get('store-id', None)

            if not store_name and not store_id:
                messages.error(request, "Store Name and Store ID are required.")
                return redirect('portal-home')
            
            Store.objects.create(
                user_id_id=request.user.id,
                store_name=store_name,
                etsy_store_id=store_id,
            )


            messages.success(request, "Store created successfully!")
            return redirect('portal-home')
        else:
            print("\nSomething Else!")
        return redirect('portal-home')
    
    return render(request, 'portal_home.html')
    