from django.shortcuts import render


def index(request):

    context = {
        'title': 'Главная',
    }

    return render(request, 'bank/index.html', context)
