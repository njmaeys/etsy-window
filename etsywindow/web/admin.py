from django.contrib import admin
from .models import Store, Listing, UserStore

admin.site.register([
    Store,
    UserStore,
    Listing,
])