# Generated by Django 4.1.7 on 2023-03-23 23:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_rename_nom_formateur_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formation',
            name='formateur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.formateur'),
        ),
    ]
