# Generated by Django 4.1.7 on 2023-03-24 00:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_participant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='cin',
            field=models.IntegerField(validators=[django.core.validators.MinLengthValidator(6)]),
        ),
    ]
