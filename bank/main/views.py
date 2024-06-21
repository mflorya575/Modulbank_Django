from django.shortcuts import render, get_object_or_404

from .models import Blog, Category, Vacancy


def index(request):

    context = {
        'title': 'Главная - Модульбанк',
    }

    return render(request, 'bank/index.html', context)


def contact(request):

    context = {
        'title': 'Контакты - Модульбанк',
    }

    return render(request, 'bank/contact.html', context)


def blog(request):
    blogs = Blog.objects.all()

    context = {
        'title': 'Блог - Модульбанк',
        'blogs': blogs,
    }

    return render(request, 'bank/blog.html', context)


def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)

    context = {
        'title': blog.title,
        'blog': blog,
    }

    return render(request, 'bank/blog_detail.html', context)


def categories_list(request):
    categories = Category.objects.all()

    context = {
        'title': 'Категории - Модульбанк',
        'categories': categories,
    }

    return render(request, 'bank/categories.html', context)


def vacancies_list(request):
    vacancies = Vacancy.objects.all()

    context = {
        'title': 'Вакансии - Модульбанк',
        'vacancies': vacancies,
    }

    return render(request, 'categories/category_vacancies.html', context)
