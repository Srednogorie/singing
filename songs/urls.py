from django.urls import path
from songs.views import SongListView

urlpatterns = [
    path('', SongListView.as_view(), name='index'),
]