from django.urls import path
from songs.views import index

urlpatterns = [
    path('', index, name='index'),
]