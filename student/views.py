from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Student
from .forms import StudentForm
# Create your views here.

def index(request):
    words = Student.objects.all()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            clean_data = form.cleaned_data
            student = Student()
            student.name = clean_data['name']
            student.sex = clean_data['sex']
            student.qq = clean_data['qq']
            student.email = clean_data['email']
            student.save()
            return  HttpResponseRedirect(reverse('index'))
    else:
        form = StudentForm()
    connext = {
        'students':words,
        'form':form,
    }
    return render(request,'index.html',context=connext)
