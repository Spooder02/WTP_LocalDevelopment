# Generated by Django 4.2.4 on 2023-08-13 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_customuser_nickname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='levels',
            field=models.OneToOneField(auto_created=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.userlevel'),
        ),
    ]
