from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Blog(models.Model):
    views = models.PositiveIntegerField(
        verbose_name='Просмотры',
        default=0)
    title = models.CharField(
        max_length=160,
        verbose_name='Заголовок',
        db_index=True)
    text = models.TextField(
        blank=True,
        verbose_name='Контент')
    image = models.ImageField(
        upload_to='image/%Y/%m/%d',
        verbose_name='Изображение',
        blank=True)
    publish_date = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата Публикации')
    author = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
        verbose_name='Автор')
    is_published = models.BooleanField(
        default=True,
        verbose_name='Состаяние публикации')
    category = models.ForeignKey(
        "Category",
        on_delete=models.DO_NOTHING,
        verbose_name='Категория',
        blank=True)
    slug = models.SlugField(
        max_length=255,
        verbose_name='Url',
        unique=True)

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
        ordering = ['-publish_date']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'slug':self.slug})


class Category(models.Model):
    title = models.CharField(
        max_length=220,
        verbose_name='Категории')
    slug = models.SlugField(
        max_length=220,
        verbose_name='Url')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['-title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})

class FilesAdmin(models.Model):
    adminupload = models.FileField(upload_to='media')
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

