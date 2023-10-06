from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from users.models import ListRegSubject
from .models import subject
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required


# Create your views here.
def showallsubject(request):
    
    return render(request, 'subjects/subject.html', {'all_subjects': subject.objects.all()})

def showRegsubject(request):
    subjectofstudent = request.user.list_subject.all()
    return render(request, 'subjects/registed.html', {'reg_subjects': subjectofstudent})

@login_required
def register(request, section, namesubject):
    # if request.method == 'POST':
    try:
        is_Reg = False
        targetS = subject.objects.get(sec_subject=section, N_subject=namesubject)
        # List_reg = ListRegSubject.objects.get(user=request.user, Subject=targetS)
        # is_Reg = List_reg is not None
        if targetS.remaining_class != 0:
            ListRegSubject.objects.create(user=request.user, Subject=targetS)
            targetS.remaining_class -= 1
            targetS.save()
            messages.success(request, "Successfully registered")
            return HttpResponseRedirect(request.headers.get('referer'))
        else :
            messages.success(request, "Section full")
            return redirect('/subjects/')
    except:
        messages.success(request, "You has My course")
        return redirect('/subjects/')
        
@login_required
def cancelReg(request, section, namesubject):
    targetS = subject.objects.get(sec_subject=section, N_subject=namesubject)
    request.user.RegSubject_set.remove(targetS)

    targetS.remaining_class += 1
    targetS.save()

    messages.success(request, "Successfully Cancel Register")
    return HttpResponseRedirect(request.headers.get('referer'))