from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Student
from .forms import StudentForm
# Create your views here.

def index(request):
    words = Student.get_all()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return  HttpResponseRedirect(reverse('index'))
    else:
        form = StudentForm()
    connext = {
        'students':words,
        'form':form,
    }
    return render(request,'index.html',context=connext)
