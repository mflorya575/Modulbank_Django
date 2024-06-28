from .models import Category


def categories_processor(request):
    return {
        'categories': Category.objects.all()
    }


def current_city_processor(request):
    city_id = request.session.get('city_id')
    if city_id:
        city = Category.objects.get(id=city_id)
    else:
        city = None
    return {'city': city}
