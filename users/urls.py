from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', include('django.contrib.auth.urls')),

    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('', views.profile, name='profile'),
]
