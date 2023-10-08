from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import CustomUser
from django.contrib.auth.decorators import login_required
from .forms import CustomUserEditForm

# Create your views here.

def index(request):
    if request.user.is_staff:
        return redirect('/admin/')
    else:
        return render(request, 'users/index.html')

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = CustomUserEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile') 
    else:
        form = CustomUserEditForm(instance=request.user)
    return render(request, 'users/edit_profile.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'user/index.html')

