from django.urls import path
from . import views

urlpatterns = [
    path('', views.showallsubject, name='allsubject'),
    path('registed', views.showRegsubject, name='registed'),
    path('unregisted/<section>/<namesubject>', views.cancelReg, name='unregisted'),
    path('register/<section>/<namesubject>', views.register, name='register'),
]
