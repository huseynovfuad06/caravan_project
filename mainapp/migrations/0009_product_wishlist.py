# Generated by Django 3.2 on 2023-06-20 16:41

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainapp', '0008_delete_wishlist'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='wishlist',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
