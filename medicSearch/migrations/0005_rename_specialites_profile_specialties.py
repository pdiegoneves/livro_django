# Generated by Django 4.2.2 on 2023-06-16 19:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('medicSearch', '0004_profile_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='specialites',
            new_name='specialties',
        ),
    ]
