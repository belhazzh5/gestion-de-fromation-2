# Generated by Django 4.1 on 2023-04-01 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0015_formation_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='formation',
            name='max_place',
            field=models.IntegerField(blank=True, default=20, null=True),
        ),
    ]
