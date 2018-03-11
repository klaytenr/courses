from django.shortcuts import render, redirect
from .models import *
# Create your views here.

def index(request):
    context = {
        'courses' : Course.objects.all()
    }
    return render(request, "course/index.html", context)

def create(request):
    Course.objects.create(name=request.POST['name'], desc=request.POST['desc'])
    return redirect('/courses')

def confirm(request, id):
    context = {
        'courses' : Course.objects.filter(id=id)
    }
    return render(request, 'course/delete.html', context)

def delete(request, id):
    this_one = Course.objects.get(id=id)
    this_one.delete()
    return redirect("/courses")