# Generated by Django 4.1.7 on 2023-03-23 23:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_formation_formateur'),
    ]

    operations = [
        migrations.RenameField(
            model_name='formateur',
            old_name='nom',
            new_name='name',
        ),
    ]