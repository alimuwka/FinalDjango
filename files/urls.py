from django.urls import path, re_path
from files.views import *
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('', cache_page(60)(IndexView.as_view()), name='home'),
    path('about/', about, name='about'),
    path('addpage/', PostCreateView.as_view(), name='add_page'),
    path('contact/', ConctactView.as_view(), name='contact'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout_user'),
    path('post/<slug:post_slug>/', PostDetailView.as_view(), name='post'),
    path('genres/<slug:genres_slug>/', GenreListView.as_view(), name='genres'),
]

