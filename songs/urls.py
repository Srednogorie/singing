from django.conf import settings
from django.urls import path
from songs.views import LatestSongListView, signup, user_profile, LatestSongDetailView, like_song, SongDelete, \
    SongUpdate, SongCreate
from django.conf.urls.static import static

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('profile/<int:pk>', user_profile, name='user-profile'),
    path('songs/<int:pk>', LatestSongDetailView.as_view(), name='song_detail'),
    path('like_song/<int:pk>', like_song, name='like-song'),
    path('delete/<int:pk>', SongDelete.as_view(), name='song-delete'),
    path('edit/<int:pk>', SongUpdate.as_view(), name='song-edit'),
    path('create', SongCreate.as_view(), name='song-create'),
    path('', LatestSongListView.as_view(), name='index'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
