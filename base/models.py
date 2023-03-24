from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator

# Create your models here.

class Formateur (models.Model):
    name = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Formation(models.Model):
    name = models.CharField(max_length=50)
    num_salle = models.CharField(max_length=50)
    date_debut = models.DateField(blank=True, null=True)
    horraire_debut = models.TimeField(blank=True, null=True)
    date_fin = models.DateField(blank=True, null=True)
    horraire_fin = models.TimeField(blank=True, null=True)
    formateur = models.ForeignKey(Formateur, on_delete=models.CASCADE)
    slug = models.SlugField(null=True,blank=True)
    def __str__(self):
        return str(self.name + " par " + self.formateur.name)

class Participant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True,blank=True)
    nom = models.CharField(max_length=50,null=True,blank=True)
    prenom = models.CharField(max_length=50,null=True,blank=True)
    cin = models.CharField(validators=[MinLengthValidator(8)],max_length=8)
    service = models.CharField(max_length=50,null=True,blank=True)
    entreprise = models.CharField(max_length=50,null=True,blank=True)
    email = models.EmailField(blank=True,null=True)
    def __str__(self):
        return str(self.nom)
    