from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import User

from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    """
    Модель категорий с вложенностью
    """
    title = models.CharField(max_length=255, verbose_name='Название категории')
    slug = models.SlugField(max_length=255, verbose_name='URL категории', blank=True)
    description = models.TextField(verbose_name='Описание категории', max_length=300)
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        db_index=True,
        related_name='children',
        verbose_name='Родительская категория'
    )

    class MPTTMeta:
        """
        Сортировка по вложенности
        """
        order_insertion_by = ('title',)

    class Meta:
        """
        Сортировка, название модели в админ панели, таблица с данными
        """
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        db_table = 'app_categories'

    def __str__(self):
        """
        Возвращение заголовка категории
        """
        return self.title


# class Post(models.Model):
#     """
#     Модель постов
#     """
#
#     STATUS_OPTIONS = (
#         ('published', 'Опубликовано'),
#         ('draft', 'Черновик')
#     )
#
#     title = models.CharField(verbose_name='Название записи', max_length=255)
#     slug = models.SlugField(verbose_name='URL', max_length=255, blank=True)
#     description = models.TextField(verbose_name='Краткое описание', max_length=500)
#     text = models.TextField(verbose_name='Полный текст записи')
#     category = TreeForeignKey('Category', on_delete=models.PROTECT, related_name='posts', verbose_name='Категория', default=1)
#     thumbnail = models.ImageField(default='default.jpg',
#         verbose_name='Изображение записи',
#         blank=True,
#         upload_to='images/thumbnails/',
#         validators=[FileExtensionValidator(allowed_extensions=('png', 'jpg', 'webp', 'jpeg', 'gif'))]
#     )
#     status = models.CharField(choices=STATUS_OPTIONS, default='published', verbose_name='Статус записи', max_length=10)
#     create = models.DateTimeField(auto_now_add=True, verbose_name='Время добавления')
#     update = models.DateTimeField(auto_now=True, verbose_name='Время обновления')
#     author = models.ForeignKey(to=User, verbose_name='Автор', on_delete=models.SET_DEFAULT, related_name='author_posts',
#                                default=1)
#     updater = models.ForeignKey(to=User, verbose_name='Обновил', on_delete=models.SET_NULL, null=True,
#                                 related_name='updater_posts', blank=True)
#     fixed = models.BooleanField(verbose_name='Прикреплено', default=False)
#
#     class Meta:
#         db_table = 'blog_post'
#         ordering = ['-fixed', '-create']
#         indexes = [models.Index(fields=['-fixed', '-create', 'status'])]
#         verbose_name = 'Статья'
#         verbose_name_plural = 'Статьи'
#
#     def __str__(self):
#         return self.title


class Blog(models.Model):
    """
    Модель постов на странице блога
    """

    STATUS_OPTIONS = (
        ('published', 'Опубликовано'),
        ('draft', 'Черновик')
    )

    title = models.CharField(verbose_name='Название записи', max_length=255)
    slug = models.SlugField(verbose_name='URL', max_length=255, blank=True)
    category = models.ForeignKey(Category, related_name='blogs', blank=True, null=True, on_delete=models.CASCADE)
    description = models.TextField(verbose_name='Краткое описание', max_length=500)
    text = models.TextField(verbose_name='Полный текст записи')
    thumbnail = models.ImageField(default='default.jpg',
        verbose_name='Изображение записи',
        blank=True,
        upload_to='images/thumbnails/',
        validators=[FileExtensionValidator(allowed_extensions=('png', 'jpg', 'webp', 'jpeg', 'gif'))]
    )
    status = models.CharField(choices=STATUS_OPTIONS, default='published', verbose_name='Статус записи', max_length=10)
    create = models.DateTimeField(auto_now_add=True, verbose_name='Время добавления')
    update = models.DateTimeField(auto_now=True, verbose_name='Время обновления')
    author = models.ForeignKey(to=User, verbose_name='Автор', on_delete=models.SET_DEFAULT, related_name='author_post',
                               default=1)
    updater = models.ForeignKey(to=User, verbose_name='Обновил', on_delete=models.SET_NULL, null=True,
                                related_name='updater_post', blank=True)
    fixed = models.BooleanField(verbose_name='Прикреплено', default=False)

    class Meta:
        db_table = 'posts_blog'
        ordering = ['-fixed', '-create']
        indexes = [models.Index(fields=['-fixed', '-create', 'status'])]
        verbose_name = 'Статья Блога'
        verbose_name_plural = 'Статьи Блога'

    def __str__(self):
        return self.title


# class BlogContent(models.Model):
#     """
#     Модель контента для постов на странице блога
#     """
#
#     CONTENT_TYPE_CHOICES = (
#         ('image', 'Изображение'),
#         ('text', 'Текст'),
#     )
#
#     blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='contents')
#     content_type = models.CharField(choices=CONTENT_TYPE_CHOICES, max_length=10)
#     image = models.ImageField(
#         upload_to='images/blog_contents/',
#         validators=[FileExtensionValidator(allowed_extensions=('png', 'jpg', 'webp', 'jpeg', 'gif'))],
#         blank=True, null=True
#     )
#     text = models.TextField(blank=True, null=True)
#
#     class Meta:
#         verbose_name = 'Контент блога'
#         verbose_name_plural = 'Контенты блога'
#
#     def __str__(self):
#         if self.content_type == 'image':
#             return f'Изображение для {self.blog.title}'
#         return f'Текст для {self.blog.title}'


class Vacancy(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(verbose_name='URL', max_length=255, blank=True)
    content = models.TextField()
    thumbnail = models.ImageField(default='default.jpg',
                                  verbose_name='Изображение вакансии',
                                  blank=True,
                                  upload_to='images/thumbnails/',
                                  validators=[
                                      FileExtensionValidator(allowed_extensions=('png', 'jpg', 'webp', 'jpeg', 'gif'))]
                                  )
    category = models.ForeignKey(Category, related_name='vacancies', on_delete=models.CASCADE)
    published_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'

    def __str__(self):
        return self.title


class BannerIndex(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.SlugField(max_length=255, unique=True, blank=True, verbose_name="Слаг")
    image = models.ImageField(upload_to='banners/', verbose_name="Изображение")
    published_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")
    is_active = models.BooleanField(default=True, verbose_name="Активен")

    class Meta:
        verbose_name = "Баннер_Главная"
        verbose_name_plural = "Баннеры_Главная"
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class BannerOpen(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.SlugField(max_length=255, unique=True, blank=True, verbose_name="Слаг")
    image = models.ImageField(upload_to='banners/', verbose_name="Изображение")
    published_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")
    is_active = models.BooleanField(default=True, verbose_name="Активен")

    class Meta:
        verbose_name = "Баннер_Открыть_счет"
        verbose_name_plural = "Баннеры_Открыть_счет"
        ordering = ['-published_at']

    def __str__(self):
        return self.title

