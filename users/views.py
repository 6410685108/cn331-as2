from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(request):
    # if not request.user.is_authenticate:
    #     return HttpResponseRedirect(reverse('login'))

    return render(request, 'users/index.html')