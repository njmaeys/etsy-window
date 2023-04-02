from django.contrib import admin
from .models import Store, User, Listing

admin.site.register([
    Store,
    User,
    Listing,
])
