# Generated by Django 4.1.7 on 2023-04-09 20:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Store',
            fields=[
                ('created_at', models.DateTimeField(auto_created=True, default=django.utils.timezone.now)),
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('etsy_store_id', models.CharField(max_length=250)),
                ('store_name', models.CharField(max_length=250)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('created_at', models.DateTimeField(auto_created=True, default=django.utils.timezone.now)),
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('listing_id', models.CharField(max_length=250)),
                ('image_url', models.CharField(max_length=250)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('store_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.store')),
            ],
        ),
    ]
