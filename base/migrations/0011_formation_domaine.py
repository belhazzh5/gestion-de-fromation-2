# Generated by Django 4.1 on 2023-03-28 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_formation_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='formation',
            name='domaine',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
