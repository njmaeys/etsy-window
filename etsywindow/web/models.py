from django.db import models


class Account(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    store_name = models.CharField(max_length=250)

class User(models.Model):
    id = models.IntegerField(primary_key=True, auto_created=True)
    account_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email_address = models.CharField(max_length=250)

class Listing(models.Model):
    listing_id = models.CharField(primary_key=True, max_length=250) # This is the id from Etsy
    account_id = models.ForeignKey(Account, on_delete=models.CASCADE)
    image_url = models.CharField(max_length=250) # This is the id from Etsy
