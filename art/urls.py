from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('images/<int:id>/', views.detail, name='detail'),
]