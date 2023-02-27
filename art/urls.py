from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view()),
    path('images/<int:id>/', views.detail, name='detail'),
    path('manage/gallery', views.ManageGalleryView.as_view()),

]