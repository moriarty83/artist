from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.IndexView.as_view()),
    path('gallery/<int:id>/', views.PieceDetail.as_view(), name='detail'),
    path('update/updaterecord/<int:id>',
         views.PieceUpdateView.as_view(), name='updaterecord'),

    path('gallery', views.GalleryView.as_view()),
    path('user/login', views.LoginView.as_view())

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
