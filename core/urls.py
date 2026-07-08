from django.urls import path
from core import views


app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('category.html', views.category, name='category'),
    path('categories/', views.category_list, name='category_list'),
    path('category/<slug:slug>/', views.category_detail, name='category_detail'),
    path('page/<slug:page_name>/', views.page, name='page'),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("shop/", views.shop, name="shop"),
    path("cart/", views.cart, name="cart"),
    path("checkout/", views.checkout, name="checkout"),
    path("login/", views.login_view, name="login"),
    path("register/", views.register, name="register"),
]