from django.urls import path
from . import views

urlpatterns = [
    path('', views.showallsubject, name='allsubject'),
    path('register/<section>/<namesubject>', views.register, name='register'),
]
