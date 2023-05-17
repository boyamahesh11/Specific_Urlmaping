from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def virat(request):
    return HttpResponse('<center><h1>Virat is very good batsman<h1><center>')

def siraj(request):
    return HttpResponse('<center><h1>Siraj very best in bowling</h1><center>')
    
