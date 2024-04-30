from django.db.models.query import QuerySet
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import redirect, render, get_object_or_404
from .models import *
from .forms import *
from django.urls import reverse_lazy
from django.views.generic import ListView,DetailView,CreateView, FormView
from .utils import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout, login


def about(request):
    return render(request, 'files/about.html', {'menu': menu, 'title': 'О сайте'})

class ConctactView(DataMixin,FormView):
    form_class = ContactForm
    template_name = 'files/contact.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        g_def = self.get_user_context(title = 'Обратная связь')
        return dict(list(context.items()) + list(g_def.items()))

    def form_valid(self, form):
        return redirect('home')

class IndexView(DataMixin,ListView):
    paginate_by = 8
    template_name = 'files/index.html'  
    context_object_name = 'posts'  
    extra_context = { 'is_homepage': True}  

    def get_queryset(self):
        return Movie.objects.filter(is_published=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        g_def = self.get_user_context(title = 'Главная страница')
        return dict(list(context.items()) + list(g_def.items()))

class PostDetailView(DataMixin,DetailView):
    model = Movie
    template_name = 'files/post.html'
    slug_url_kwarg = 'post_slug'
    context_object_name = 'post'

    def get_context_data(self,*,object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        g_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(g_def.items()))


class GenreListView(DataMixin, ListView):
    model = Movie
    template_name = 'files/index.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        genre = get_object_or_404(Genre, slug=self.kwargs['genres_slug'])
        return Movie.objects.filter(genres=genre, is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        genre = get_object_or_404(Genre, slug=self.kwargs['genres_slug'])
        context['title'] = f'Фильмы в жанре {genre.name}'
        context['menu'] = menu
        context['is_homepage'] = True
        return context


class PostCreateView(LoginRequiredMixin, DataMixin,CreateView):
    form_class = AddPostForm
    template_name = 'files/addmovie.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')
    raise_exception = True

    def get_context_data(self,*,object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        g_def = self.get_user_context(title='Добавление фильма')
        return dict(list(context.items()) + list(g_def.items()))


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'files/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self,*,object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        g_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(g_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user, backend='django.contrib.auth.backends.ModelBackend')
        return redirect('home')
    
class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'files/login.html'

    def get_context_data(self,*,object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        g_def = self.get_user_context(title='Авторизация')
        return dict(list(context.items()) + list(g_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Не там ищешь, родной. ЛОВИ 404</h1>")


def logout_user(request):
    logout(request)
    return redirect('login')