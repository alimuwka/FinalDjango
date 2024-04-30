from django.contrib import admin
from .models import *

class MovieAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}

class GenreAdmin(admin.ModelAdmin):
    list_display = ('id','name')
    list_display_links = ('id','name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}

admin.site.register(Genre, GenreAdmin)
admin.site.register(Actor)
admin.site.register(Director)
admin.site.register(Company)
admin.site.register(Country)
admin.site.register(Favorite)
admin.site.register(Movie, MovieAdmin)

