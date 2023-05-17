from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def dhoni(request):
    return HttpResponse('<center><h1>Dhoni is india captain</h1></center>')


def pandya(request):
    return HttpResponse('<center><h1>Pandya is most dangeros bowler in india')
