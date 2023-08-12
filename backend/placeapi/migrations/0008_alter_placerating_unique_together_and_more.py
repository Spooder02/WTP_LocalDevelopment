# Generated by Django 4.2.4 on 2023-08-13 00:01

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('placeapi', '0007_rename_user_id_placerating_user_placerating_place_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='placerating',
            unique_together={('user', 'rating')},
        ),
        migrations.RemoveField(
            model_name='placerating',
            name='place',
        ),
    ]
