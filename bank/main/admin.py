from django.contrib import admin

from mptt.admin import DraggableMPTTAdmin
from django_mptt_admin.admin import DjangoMpttAdmin
from .models import Category, Blog, Vacancy, BannerIndex, BannerOpen


@admin.register(Category)
class CategoryAdmin(DjangoMpttAdmin):
    """
    Админ-панель модели категорий
    """
    prepopulated_fields = {'slug': ('title',)}


# admin.site.register(Post)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    """
    Админ-панель модели записей
    """
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    """
    Админ-панель модели записей
    """
    prepopulated_fields = {'slug': ('title',)}


@admin.register(BannerIndex)
class BannerIndexAdmin(admin.ModelAdmin):
    """
    Админ-панель модели баннеров
    """
    prepopulated_fields = {'slug': ('title',)}


@admin.register(BannerOpen)
class BannerOpenAdmin(admin.ModelAdmin):
    """
    Админ-панель модели баннеров
    """
    prepopulated_fields = {'slug': ('title',)}
