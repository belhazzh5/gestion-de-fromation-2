from django.shortcuts import render,get_object_or_404,redirect
from .models import Formation,Participant
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

# Create your views here.
# def home(request):
#     context = {
#         'formations': Formation.objects.all()
#     }
#     return render(request, "base/index.html",context)

class FormationListView(ListView):
    model = Formation
    template_name = "base/index.html"
    context_object_name = "myFormation"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['nbParticipant'] =  2
        return context
    
class FormationDetailView(DetailView):
    model = Formation
    template_name = "base/course-details.html"
    context_object_name = "formation"


@login_required
def join_formation(request, slug):
    formation = get_object_or_404(Formation, slug=slug)
    participant = Participant.objects.get(user=request.user)
    if participant:
        if participant in formation.participant.all():
            messages.error(request, "You have already joined this formation.")
            return redirect('home')
        else:
            formation.participant.add(participant)
            messages.success(request, "You have joined the formation successfully.")
    else:
        participant = Participant.objects.create(user=request.user,cin='14501407')
        formation.participant.add(participant)
        messages.success(request, "You have joined the formation successfully.")
    formation.save()
    return redirect('formation', slug=formation.slug)

# @login_required
def dash(request):
    context = {}
    return render(request, "base/dash.html",context)