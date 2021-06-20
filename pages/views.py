from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request):
    return HttpResponse("<h1>Hello World</h1>") #string of HTML

def contact_view(request):
    return HttpResponse("<h1>Contact Page</h1>") #string of HTML