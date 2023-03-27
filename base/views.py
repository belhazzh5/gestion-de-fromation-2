from django.shortcuts import render
from .models import Formation
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    context = {
        'formations': Formation.objects.all()
    }
    return render(request, "base/index.html",context)

# @login_required
def dash(request):
    context = {}
    return render(request, "base/dash.html",context)