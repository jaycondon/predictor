from django.urls import path

from . import views

urlpatterns = [
    path('scrape', views.index, name='index'),
    path('', views.hello, name='hello')
]