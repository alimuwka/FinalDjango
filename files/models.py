from django.db import models
from django.urls import reverse

class Genre(models.Model):
    name = models.CharField(max_length=100) 
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'    

    def get_absolute_url(self):
        return reverse('genres', kwargs={'genres_slug':self.slug})

class Director(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.first_name + " " + self.last_name}'
    class Meta:
        verbose_name = 'Режиссер'
        verbose_name_plural = 'Режиссеры'    

class Actor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100) 
    def __str__(self):
        return f'{self.first_name + " " + self.last_name}'
    class Meta:
        verbose_name = 'Актер'
        verbose_name_plural = 'Актеры'    

class Country(models.Model):
    name = models.CharField(max_length=100) 
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'    
        

class Company(models.Model):
    name = models.CharField(max_length=100) 
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Киностудия'
        verbose_name_plural = 'Киностудии'   


class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_year = models.PositiveIntegerField(null = True, blank = True)
    description = models.TextField()
    rating = models.DecimalField(max_digits = 3 , decimal_places = 1, null = True, blank = True)
    genres = models.ManyToManyField(Genre)
    directors = models.ManyToManyField(Director)
    actors = models.ManyToManyField(Actor)
    country = models.ForeignKey(Country, on_delete=models.CASCADE,null = True, blank = True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE,null = True, blank = True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото")
    video = models.FileField(upload_to="videos/%Y/%m%d", verbose_name="Видео")
    created_date = models.DateTimeField(auto_now_add = True)
    update_date = models.DateTimeField(auto_now = True)
    is_published = models.BooleanField(default=True)
    views = models.IntegerField(default=0, null=True, blank=True)
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
    
    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug':self.slug})


class Favorite(models.Model):


    movie = models.ForeignKey(
        Movie,
        on_delete=models.CASCADE
    )
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} --> {self.movie}'
    
    class Meta:
        verbose_name = 'Избранный'
        verbose_name_plural = 'Избранныe'
