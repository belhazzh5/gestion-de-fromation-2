from django.shortcuts import render,get_object_or_404,redirect
from .models import Formation,Participant,Profile,Activity
from .forms import UserRegisterForm,ProfileForm,FormationForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse,reverse_lazy
from django.contrib.auth.models import User
import datetime

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
    def get(self, request, *args, **kwargs):
        # Get the logged in user
        user = self.request.user

        # Call the parent's get() method to get the context data dictionary
        context = super().get(request, *args, **kwargs).context_data

        # Add the user to the context data dictionary
        context['user'] = user
        if user.is_authenticated:
            try:
                context['participant_user'] = Participant.objects.get(user=user)
            except:
                pass
        # Return the updated context data dictionary
        return self.render_to_response(context)
    
class FormationDetailView(DetailView):
    model = Formation
    template_name = "base/course-details.html"
    context_object_name = "formation"


class FormationCreateView(CreateView):
    form_class = FormationForm
    template_name = "base/create_formation.html"
    queryset = Formation.objects.none()
    def get_success_url(self):
        return reverse_lazy('home')
class FormationUpdate(UpdateView):
    model = Formation
    fields = ("name","num_salle","domaine","description","date_debut","horraire_debut","date_fin","formateur","max_places","image")
    template_name = "base/update_formation.html"    
    def get_success_url(self):
        return reverse_lazy('home')

class FormationDelete(DeleteView):
    model = Formation
    template_name = "base/delete_formation.html"
    def get_success_url(self):
        return reverse_lazy('home')

@login_required
def join_formation(request, slug):
    formation = get_object_or_404(Formation, slug=slug)
    participant = Participant.objects.get(user=request.user)
    if participant:
        if participant in formation.participant.all():
            messages.error(request, "You have already joined this formation.")
            return reverse_lazy('home')
        else:
            formation.participant.add(participant)
            messages.success(request, "You have joined the formation successfully.")
            Activity.objects.create(name=f'participer a la formation {formation.name}',user=request.user)
    else:
        participant = Participant.objects.create(user=request.user)
        formation.participant.add(participant)
        messages.success(request, "You have joined the formation successfully.")
        Activity.objects.create(name=f'participer a la formation {formation.name}',user=request.user)
    formation.save()
    return redirect('profile')

@login_required
def leave_formation(request, slug):
    formation = get_object_or_404(Formation, slug=slug)
    participant = Participant.objects.get(user=request.user)
    if participant:
        if participant in formation.participant.all():
            formation.participant.remove(participant)
            messages.success(request, "You have left the formation successfully.")
            Activity.objects.create(name=f'annuler l"inscription de formation {formation.name}',user=request.user)
        else:
            messages.error(request, "You are not part of this formation.")
    else:
        messages.error(request, "You are not a registered participant.")
        return redirect('register')
    formation.save()
    return redirect('profile')


def signUpView(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = User.objects.get(username=request.POST.get('username'))
            if user:
                Participant.objects.create(user=user,email=user.email)
                Profile.objects.create(user=user,name=user.username,email=user.email)
            return redirect(reverse_lazy('login'))
    context = {
        'form':form
    }
    return render(request,'registration/register.html',context)

@login_required
def profile(request):
    try:
        form = ProfileForm(instance=Profile.objects.get(user=request.user))
    except:
        form={}
    if request.method == 'POST':
        form = ProfileForm(request.POST,request.FILES,instance=Profile.objects.get(user=request.user))
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('profile'))
    context = {}
    if request.user:
        context['profile'] = Profile.objects.get(user=request.user)
        participant = Participant.objects.get(user=request.user)
        context['formations'] = participant.formation_set.all()
        context['activities'] = Activity.objects.filter(user=request.user).order_by('-timestamp')[:4]
        context['form'] = form
    return render(request, 'base/profile.html',context)
