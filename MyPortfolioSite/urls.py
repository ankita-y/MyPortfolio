from django.contrib import admin
from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [
    path('',views.index, name='MyPortfolio'),
    path('pythonproject/',views.pythonproject,name='Pythonprojects'),
    path('djangoproject/',views.djangoproject,name='DjangoProjects')
    
]

