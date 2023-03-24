from django.contrib import admin
from .models import Formation,Formateur,Participant
# Register your models here.
admin.site.register(Formation)
admin.site.register(Formateur)
admin.site.register(Participant)
