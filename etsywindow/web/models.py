from django.db import models
from django.utils import timezone


class Store(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    etsy_store_id = models.CharField(max_length=250)
    store_name = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_created=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)


class User(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email_address = models.CharField(max_length=250, null=False)
    created_at = models.DateTimeField(auto_created=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)


class UserStore(models.Model):
    store_id = models.ForeignKey(Store, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['store_id', 'user_id'], name='unique_store_user')
        ]


class Listing(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    listing_id = models.CharField(max_length=250)
    store_id = models.ForeignKey(Store, on_delete=models.CASCADE)
    image_url = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_created=True, default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
