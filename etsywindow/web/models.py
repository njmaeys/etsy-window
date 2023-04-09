from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Store(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    etsy_store_id = models.CharField(max_length=250)
    store_name = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_created=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)


class Listing(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    listing_id = models.CharField(max_length=250)
    store_id = models.ForeignKey(Store, on_delete=models.CASCADE)
    image_url = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_created=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
