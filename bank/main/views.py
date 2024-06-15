from django.shortcuts import render


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
