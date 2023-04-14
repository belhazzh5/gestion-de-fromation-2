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
    cin = models.CharField(validators=[MinLengthValidator(8)],max_length=8,blank=True, null=True)
    service = models.CharField(max_length=50,null=True,blank=True)
    email = models.EmailField(blank=True,null=True)
    entreprise = models.CharField(max_length=50,null=True,blank=True)

    def __str__(self):
        if self.user:
            return str(self.user.username)
        return str(self.user)

class Formation(models.Model):
    name = models.CharField(max_length=50)
    num_salle = models.CharField(max_length=50)
    domaine = models.CharField(max_length=50,blank=True,null=True)
    description = models.TextField(blank=True, null=True)
    date_debut = models.DateField(blank=True, null=True)
    horraire_debut = models.TimeField(blank=True, null=True)
    date_fin = models.DateField(blank=True, null=True)
    formateur = models.ForeignKey(Formateur, on_delete=models.CASCADE)
    max_places = models.IntegerField(blank=True, null=True,default=20)
    image = models.ImageField(upload_to="images-formation",blank=True, null=True)
    participant = models.ManyToManyField(Participant,blank=True)
    slug = models.SlugField(null=True,blank=True)
    def __str__(self):
        return str(self.name + " par " + self.formateur.name)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,blank=True, null=True)
    email = models.EmailField(max_length=254,blank=True, null=True)
    image = models.ImageField(upload_to="images/users/",blank=True, null=True)
    name = models.CharField(max_length=50,blank=True, null=True)
    def __str__(self):
        return str(self.user.username)

class Activity(models.Model):
    name = models.CharField(max_length=50,blank=True, null=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True,blank=True, null=True)
    def __str__(self):
        return self.user.username

class Notification(models.Model):
    name = models.CharField(max_length=50,blank=True, null=True)
    timestamp = models.DateField(auto_now_add=True)
    

@receiver(pre_save, sender=Formation)
def pre_save_receiver(sender, instance, *args, **kwargs):
   if not instance.slug:
       instance.slug = unique_slug_generator(instance)