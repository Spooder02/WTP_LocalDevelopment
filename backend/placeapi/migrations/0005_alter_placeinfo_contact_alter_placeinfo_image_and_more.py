# Generated by Django 4.2.4 on 2023-08-11 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('placeapi', '0004_delete_placesubinfo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placeinfo',
            name='contact',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='placeinfo',
            name='image',
            field=models.ImageField(null=True, upload_to='placeinfo_image'),
        ),
        migrations.AlterField(
            model_name='placeinfo',
            name='time',
            field=models.CharField(max_length=100, null=True),
        ),
    ]