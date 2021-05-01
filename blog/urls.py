from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views



urlpatterns = [
    path('', views.showblog, name='showblog'),
    path('<int:post_id>/', views.post_details, name='post_details'), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)