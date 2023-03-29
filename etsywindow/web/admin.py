from django.contrib import admin
from .models import Account, User, Listing

admin.site.register([
    Account,
    User,
    Listing,
])
