from django.shortcuts import render
from django.http import HttpResponse
from app.models import *
# Create your views here.
def krishna(request):
    S=input('enter school name:')
    C=input('enter collage name:')
    D=input('enter group :')
    SN=School.objects.get_or_create(school_name=S)[0]
    IN=Inter.objects.get_or_create(school_name=SN,collage_name=C)[0]
    DG=Degree.objects.get_or_create(collage_name=IN,group=D)[0]




    return HttpResponse('this is creating models using views')