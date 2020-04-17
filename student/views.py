from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from .models import Student
from .forms import StudentForm


def index(request):
    words = Student.get_all()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
    else:
        form = StudentForm()
    connext = {
        'students': words,
        'form': form,
    }
    return render(request, 'index.html', context=connext)


class IndexView(View):

    def get_connext(self):
        student = Student.objects.all()
        context = {
            'student': student,
        }
        return context

    def get(self, request):
        context = self.get_connext()
        form = StudentForm()
        context.setdefault('form', form)
        return render(request, 'index.html', context=context)

    def post(self, request):
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('index'))
        context = self.get_connext()
        context.setdefault('form', form)
        return render(request, 'index.html', context=context)
