from django.shortcuts import render
from .models import Formation
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
# def home(request):
#     context = {
#         'formations': Formation.objects.all()
#     }
#     return render(request, "base/index.html",context)

class FormationListView(LoginRequiredMixin,ListView):
    model = Formation
    template_name = "base/index.html"
    context_object_name = "myFormation"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nbParticipant'] =  2
        return context
    
    

# @login_required
def dash(request):
    context = {}
    return render(request, "base/dash.html",context)