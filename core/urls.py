from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


app_name = 'core'

#urlpatterns = [path('urls/', views.index)]
urlpatterns = [path('', views.index, name='index'),]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)