from django.db import models

# Create your models here.
class Formation(models.Model):
    name = models.CharField(max_length=50)
    num_salle = models.CharField(max_length=50)

    def __str__(self):
        return self.name

