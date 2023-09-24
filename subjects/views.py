from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .models import subject
from django.contrib import messages
from django.urls import reverse


# Create your views here.
def showallsubject(request):
    return render(request, 'subjects/subject.html', {'all_subjects': subject.objects.all()})

def register(request, section, namesubject):
        targetS = subject.objects.get(sec_subject=section, N_subject=namesubject)
        if targetS.remaining_class != 0:
            targetS.remaining_class -= 1
            targetS.save()
            messages.success(request, "Successfully registered")
            return redirect('http://127.0.0.1:8000/subjects/')
        else :
            messages.success(request, "Section full")
            return redirect('http://127.0.0.1:8000/subjects/')