from django.urls import path
from . import views

urlpatterns = [
    path('', views.showallsubject, name='allsubject'),
    path('registed', views.showRegsubject, name='registed'),
    path('unregisted/<sID>', views.cancelReg, name='unregisted'),
    path('register/<sID>', views.register, name='register'),
]
