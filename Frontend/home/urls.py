from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('model', views.model, name='model'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('blog', views.blog, name='blog'),
    path('blogpost/<str:slug>', views.blogpost, name='blogpost'),
    path('category/<str:category>', views.category, name='category'),
    path('categories/', views.categories, name='categories'),
    path('search/', views.search, name='search'),
    path('thanks', views.thanks, name='thanks'),
]