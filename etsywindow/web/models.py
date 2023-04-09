from django.db import models
from django.utils import timezone
from django.conf import settings


class Store(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    etsy_store_id = models.CharField(max_length=250)
    store_name = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_created=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)


class UserStore(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['store', 'user'], name='unique_store_user')
        ]


class Listing(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    listing_id = models.CharField(max_length=250)
    store_id = models.ForeignKey(Store, on_delete=models.CASCADE)
    image_url = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_created=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)