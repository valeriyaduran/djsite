from django.db.models import *

# Create your models here.
from django.urls import reverse


class Women(Model):
    title = CharField(max_length=255, verbose_name='Заголовок')
    slug = SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    content = TextField(blank=True, verbose_name='Текст статьи')
    photo = ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото')
    time_create = DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = DateTimeField(auto_now=True, verbose_name='Время изменения')
    is_published = BooleanField(default=True, verbose_name='Публикация')
    cat = ForeignKey('Category', on_delete=PROTECT, verbose_name='Категории')

# для чтения записей  из базы в удобном виде, тут будет выводиться список тайтлов
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Известные женщины'
        verbose_name_plural = 'Известные женщины'
        ordering = ['time_create', 'title']


class Category(Model):
    name = CharField(max_length=100, db_index=True, verbose_name='Категория')
    slug = SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']