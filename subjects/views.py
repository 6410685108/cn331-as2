from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from users.models import ListRegSubject
from .models import subject
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def showallsubject(request):
    return render(request, 'subjects/subject.html', {'all_subjects': subject.objects.all()})

@login_required
def showRegsubject(request):
    subjectofstudent = request.user.list_subject.all()
    return render(request, 'subjects/registed.html', {'reg_subjects': subjectofstudent})

@login_required
def register(request, sID):
    try:
        targetS = subject.objects.get(subjectID=sID)
        if targetS.remaining_class != 0:
            ListRegSubject.objects.create(user=request.user, Subject=targetS)
            targetS.remaining_class -= 1
            targetS.save()
            messages.success(request, "Registration successful")
            return HttpResponseRedirect(request.headers.get('referer'))
        else :
            messages.success(request, "Quota full")
            return redirect('/subjects/')
    except:
        messages.success(request, "You already have this quota.")
        return redirect('/subjects/')
        
@login_required
def cancelReg(request, sID):
    targetS = subject.objects.get(subjectID=sID)
    request.user.RegSubject_set.remove(targetS)

    targetS.remaining_class += 1
    targetS.save()

    messages.success(request, "Cancellation successful")
    return HttpResponseRedirect(request.headers.get('referer'))