from datetime import timezone
from unidecode import unidecode
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class BlogPost(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name='Контент')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL', blank=True)
    date_posted = models.DateTimeField(auto_now_add=True, verbose_name='Время выкладывания')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    image = models.ImageField(upload_to='blog_images/', verbose_name='Изображение', blank=True, null=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unidecode(self.title))
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Пост блога"

    def get_absolute_url(self):
        return reverse('detail', kwargs={'post_slug': self.slug})
