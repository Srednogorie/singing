from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
from songs.models import Song, CustomUser, Like


class SongAdmin(admin.ModelAdmin):
    pass


class LikeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Song, SongAdmin)
admin.site.register(Like, LikeAdmin)
admin.site.register(CustomUser, UserAdmin)
