from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from .models import Artist, Release
from .forms import ReleaseForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class Home(LoginView):
    template_name = 'home.html'

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('record-index')
        else:
            error_message = 'Invalid Field'
    form = UserCreationForm()
    return render(request, 'signup.html', {
        'form': form,
        'error_message': error_message
    })

@login_required
def add_release(request):
    form = ReleaseForm(request.POST)
    if form.is_valid():
        new_release = form.save(commit=False)
        new_release.save()

class ArtistIndex(ListView):
    model = Artist

class ArtistDetail(DetailView):
    model = Artist


class ArtistCreate(LoginRequiredMixin, CreateView):
    model = Artist
    fields = ['name', 'members', 'bio', 'isActive', 'img']
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ArtistUpdate(LoginRequiredMixin, UpdateView):
    model = Artist
    fields = ['members', 'bio', 'isActive', 'img']

class ArtistDelete(LoginRequiredMixin, DeleteView):
    model = Artist
    success_url = '/artists/'

class ReleaseList(ListView):
    model = Release

class ReleaseDetail(DetailView):
    model = Release

class ReleaseCreate(LoginRequiredMixin, CreateView):
    model = Release
    form_class = ReleaseForm
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ReleaseUpdate(LoginRequiredMixin, UpdateView):
    model = Release
    form_class = ReleaseForm

class ReleaseDelete(LoginRequiredMixin, DeleteView):
    model = Release
    success_url = '/releases/'