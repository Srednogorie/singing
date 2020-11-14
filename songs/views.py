from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from songs.models import Song


class SongListView(ListView):
    template_name = 'index.html'

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Song.objects.all()
        return Song.objects.order_by('-created')[:5]
