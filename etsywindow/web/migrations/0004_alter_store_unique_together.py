# Generated by Django 4.1.7 on 2023-04-16 14:00

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web', '0003_listing_title'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='store',
            unique_together={('user_id', 'etsy_store_id')},
        ),
    ]
