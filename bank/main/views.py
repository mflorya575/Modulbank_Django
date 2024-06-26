from django.shortcuts import render, get_object_or_404

from .models import Blog, Category, Vacancy, BannerIndex, BannerOpen, BannerCredit, BannerBank, BannerPartner


def index(request):
    vacancies = Vacancy.objects.all()
    blogs = Blog.objects.all()
    banners = BannerIndex.objects.all()

    context = {
        'title': 'Главная - Модульбанк',
        'vacancies': vacancies,
        'blogs': blogs,
        'banners': banners,
    }

    return render(request, 'bank/index.html', context)


def about(request):

    context = {
        'title': 'О нас - Модульбанк',
    }

    return render(request, 'bank/about.html', context)


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


# def categories_list(request):
#     categories = Category.objects.all()
#
#     context = {
#         'title': 'Категории - Модульбанк',
#         'categories': categories,
#     }
#
#     return render(request, 'bank/categories.html', context)


def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    vacancies = Vacancy.objects.filter(category=category)

    context = {
        'title': category.title,
        'vacancies': vacancies,
        'category': category,
    }

    return render(request, 'bank/category_detail.html', context)


def vacancies_list(request):
    vacancies = Vacancy.objects.all()

    context = {
        'title': 'Вакансии - Модульбанк',
        'vacancies': vacancies,
    }

    return render(request, 'categories/category_vacancies.html', context)


def vacancy_detail(request, slug):
    vacancy = get_object_or_404(Vacancy, slug=slug)

    context = {
        'title': vacancy.title,
        'vacancy': vacancy,
    }

    return render(request, 'categories/vacancy_detail.html', context)


def partner_program(request):
    banners = BannerPartner.objects.all()

    context = {
        'title': 'Партнерская программа - Модульбанк',
        'banners': banners,
    }

    return render(request, 'bank/partner_program.html', context)


def open_score(request):
    bannersopen = BannerOpen.objects.all()

    context = {
        'title': 'Открыть счет - Модульбанк',
        'bannersopen': bannersopen,
    }

    return render(request, 'bank/open_score.html', context)


def bank_garant(request):

    context = {
        'title': 'Банковские гарантии - Модульбанк',
    }

    return render(request, 'bank/bank_garant.html', context)


def credit(request):
    banners = BannerCredit.objects.all()

    context = {
        'title': 'Кредиты - Модульбанк',
        'banners': banners,
    }

    return render(request, 'bank/credit.html', context)
