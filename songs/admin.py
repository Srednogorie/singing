from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from songs.models import Song, CustomUser


class SongAdmin(admin.ModelAdmin):
    pass


admin.site.register(Song, SongAdmin)
admin.site.register(CustomUser, UserAdmin)
