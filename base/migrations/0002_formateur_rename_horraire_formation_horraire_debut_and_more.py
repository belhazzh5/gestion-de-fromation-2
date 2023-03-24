# Generated by Django 4.1.7 on 2023-03-23 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Formateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=50)),
                ('prenom', models.CharField(max_length=50)),
            ],
        ),
        migrations.RenameField(
            model_name='formation',
            old_name='horraire',
            new_name='horraire_debut',
        ),
        migrations.AddField(
            model_name='formation',
            name='horraire_fin',
            field=models.TimeField(blank=True, null=True),
        ),
    ]