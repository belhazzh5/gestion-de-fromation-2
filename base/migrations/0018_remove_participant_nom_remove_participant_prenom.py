# Generated by Django 4.1 on 2023-04-01 23:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0017_rename_max_place_formation_max_places'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='participant',
            name='nom',
        ),
        migrations.RemoveField(
            model_name='participant',
            name='prenom',
        ),
    ]
