from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField('Заголовок поста', max_length=450) #заголовок поста
    author = models.ForeignKey( #автор поста
        'auth.User',
        on_delete=models.CASCADE,
    )
    body = models.TextField('Текст поста') #поле поста

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('home')

