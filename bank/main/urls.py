from django.urls import path
from . import views


app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),

    path('set_city/<int:city_id>/', views.set_city, name='set_city'),

    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),

    # path('categories/', views.categories_list, name='categories_list'),
    path('category/<slug:slug>/', views.category_detail, name='category_detail'),

    # path('vacancies/', views.vacancies_list, name='vacancies_list'),
    path('vacancies/', views.vacancies_list, name='vacancies_list'),

    path('vacancy/<slug:slug>/', views.vacancy_detail, name='vacancy_detail'),

    path('city/<slug:city_slug>/', views.city_detail, name='city_detail'),

    path('partner-program/', views.partner_program, name='partner_program'),
    path('open-score/', views.open_score, name='open_score'),
    path('bank-garant/', views.bank_garant, name='bank_garant'),
    path('credit/', views.credit, name='credit'),
]
