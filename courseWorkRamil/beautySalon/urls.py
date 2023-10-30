from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'beautySalon'

urlpatterns = [
    path('', views.index, name='index'),
    path('user_profile/<int:user_id>', views.show_user_profile, name='user_profile'),
    path('masters/', views.show_all_masters, name='all_masters'),
    path('services/', views.show_all_services, name='all_services'),
    path('one_master/<int:user_id>', views.show_user_profile, name='one_master'),
    path('make_appointment/<int:service_id>', views.make_appointment, name='make_appointment'),
    path('close_appointment/<int:appointment_id>', views.close_appointment, name='close_appointment'),
    path('set_rating/', views.set_rating, name='set_rating'),
    path('articles/', views.show_all_articles, name='all_articles'),
    path('one_article/<int:article_id>', views.show_one_article, name='one_article'),
    path('add_comment/<int:master_id>', views.add_comment, name='add_comment'),
    path('detele_comment/<int:comment_id>', views.delete_comment, name='delete_comment'),
]

handler404 = 'beautySalon.views.error_404'