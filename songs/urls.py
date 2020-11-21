from django.conf import settings
from django.urls import path
from songs.views import SongListView, signup, user_profile
from django.conf.urls.static import  static

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('profile/<int:pk>', user_profile, name='user-profile'),
    path('', SongListView.as_view(), name='index'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
