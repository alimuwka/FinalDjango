from .models import *
from django.db.models import Count


menu = [
    {'title': "О сайте", 'url_name': 'about'},
    {'title': "Добавить фильм", 'url_name': 'add_page'},
    {'title': "Обратная связь", 'url_name': 'contact'},
]


class DataMixin:
    paginate_by = 4
    def get_user_context(self, **kwargs):
        context = kwargs
        genres_with_movies = Genre.objects.filter(movie__is_published=True).distinct()

        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)

        context['menu'] = user_menu
        context['genres'] = genres_with_movies
        return context