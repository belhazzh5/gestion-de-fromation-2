# Generated by Django 4.1 on 2023-05-23 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0035_formation_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='formateur',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]