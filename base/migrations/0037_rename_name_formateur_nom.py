# Generated by Django 4.1 on 2023-05-23 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0036_formateur_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='formateur',
            old_name='name',
            new_name='nom',
        ),
    ]
