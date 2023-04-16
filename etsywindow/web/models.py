from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

"""
Simple note to myself. Put this somewhere later.
It would be cool to allow the user to set an order
for their listings. Should be as simple as putting
a `priority` on the listings table. This will be interesting
to implement tho 

Another cool idea would be to allow the user to
select if they want to display an item or not. Should
be able to put a `display` bool column on the listing
and only return back where display == True
"""

class Store(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    etsy_store_id = models.CharField(max_length=250)
    store_name = models.CharField(max_length=250)
    store_url = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_created=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)


class Listing(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    listing_id = models.CharField(max_length=250)
    store_id = models.ForeignKey(Store, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    image_url = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_created=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
