# Create your views here.
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView

from songs.forms import SignUpForm, UserProfileForm
from songs.models import Song, CustomUser, Like
from django.http import Http404, JsonResponse
from django.db import IntegrityError


class LatestSongListView(ListView):
    template_name = 'index.html'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Song.objects.all()
        return Song.objects.order_by('-created')[:3]


class LatestSongDetailView(DetailView):
    template_name = 'song_detail.html'
    model = Song

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            return redirect('login')
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def get_object(self, queryset=None):
        obj = super(LatestSongDetailView, self).get_object(queryset)
        if not self.request.user.is_authenticated:
            latest_songs = Song.objects.order_by('-created')[:3]
            if obj in latest_songs:
                return obj
            else:
                raise Http404
        return obj

    def get_context_data(self, **kwargs):
        context = super(LatestSongDetailView, self).get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['can_like'] = Like.objects.filter(
                user=self.request.user, song=context['song']
            ).exists()
        return context


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


def like_song(request, pk):
    song = Song.objects.get(pk=pk)
    try:
        Like.objects.create(song=song, user=request.user)
        return JsonResponse({"SUCCESS": "You liked this song."})
    except IntegrityError:
        return JsonResponse({"ERROR": "You cannot like a song multiple times."})


class SongDelete(DeleteView):
    model = Song
    success_url = reverse_lazy('index')
    template_name = 'song_confirm_delete.html'


class SongUpdate(UpdateView):
    model = Song
    fields = ['name', 'band', 'lyrics', 'video']
    template_name = 'song_edit.html'

    def get_success_url(self):
        return reverse('song_detail', kwargs={'pk': self.kwargs['pk']})


class SongCreate(CreateView):
    model = Song
    fields = ['name', 'band', 'lyrics', 'video']
    template_name = 'song_create.html'
