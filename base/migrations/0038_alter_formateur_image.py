# Generated by Django 4.1 on 2023-05-23 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0037_rename_name_formateur_nom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formateur',
            name='image',
            field=models.ImageField(blank=True, default='images/az.jpg', null=True, upload_to='images-formation'),
        ),
    ]
