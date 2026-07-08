from django.urls import path
from core import views


app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('category.html', views.category, name='category'),
    path('categories/', views.category_list, name='category_list'),
    path('category/<slug:slug>/', views.category_detail, name='category_detail'),
]