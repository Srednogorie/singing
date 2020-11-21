# Create your views here.
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.views.generic import ListView

from songs.forms import SignUpForm, UserProfileForm
from songs.models import Song, CustomUser


class SongListView(ListView):
    template_name = 'index.html'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Song.objects.all()
        return Song.objects.order_by('-created')[:5]


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def user_profile(request, pk):
    user = CustomUser.objects.get(pk=pk)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user-profile', pk=pk)
    else:
        form = UserProfileForm(instance=user)
    return render(request, 'profile.html', {'form': form})
