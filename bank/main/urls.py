from django.urls import path
from . import views


app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),

    path('vacancies/', views.vacancies_list, name='vacancies_list'),
    path('vacancy/<slug:slug>/', views.vacancy_detail, name='vacancy_detail'),

    path('partner_program/', views.partner_program, name='partner_program'),
]
