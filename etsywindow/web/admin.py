from django.contrib import admin
from .models import Store, Listing

admin.site.register([
    Store,
    Listing,
])