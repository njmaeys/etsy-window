from django.shortcuts import render, redirect

from ..models import Store
from .utils.etsy_helper import get_shop_data


def manage_store(request):
    if not request.user.is_authenticated:
        return redirect('login')
    
    print("\n### HERE ###")
    print(request)

    return render(request, 'manage_store.html')