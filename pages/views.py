from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def homepage_home(request):
    return HttpResponse("<h1>Hello World</h1>") #string of HTML