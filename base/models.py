from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.dispatch import receiver
from django.db.models.signals import pre_save
from .utils import unique_slug_generator
# Create your models here.

class Formateur (models.Model):
    name = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    image = models.ImageField(upload_to="images-formation",blank=True, null=True)
    def __str__(self):
        return self.name
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
class Formation(models.Model):
    name = models.CharField(max_length=50)
    num_salle = models.CharField(max_length=50)
    domaine = models.CharField(max_length=50,blank=True,null=True)
    date_debut = models.DateField(blank=True, null=True)
    horraire_debut = models.TimeField(blank=True, null=True)
    date_fin = models.DateField(blank=True, null=True)
    formateur = models.ForeignKey(Formateur, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images-formation",blank=True, null=True)
    participant = models.ManyToManyField(Participant,blank=True)
    slug = models.SlugField(null=True,blank=True)
    def __str__(self):
        return str(self.name + " par " + self.formateur.name)

    
@receiver(pre_save, sender=Formation)
def pre_save_receiver(sender, instance, *args, **kwargs):
   if not instance.slug:
       instance.slug = unique_slug_generator(instance)