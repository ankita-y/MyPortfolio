from django.shortcuts import render
from django.http import HttpResponse
from .models import Portfolio, PythonProjects
from math import ceil

# Create your views here.
def index(request):
    portfolio = Portfolio.objects.all()
    n = len(portfolio)
    nslides = n//4 + ceil((n/4)-(n//4))
    params = {'no_of_slide':nslides,'range':range(1,nslides),'portfolio':portfolio}
    return render(request,'index.html',params)

def pythonproject(request):
    pyproject = PythonProjects.objects.all()
    return render(request,'Pythonprojects.html',{'pyproject':pyproject})


def djangoproject(request):
    pyproject = PythonProjects.objects.all()
    return render(request,'DjangoProjects.html',{'pyproject':pyproject})