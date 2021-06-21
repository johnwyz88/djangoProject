from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request, *args, **kwargs):
    # print(args, kwargs)
    # print(request.user)
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})

def about_view(request, *args, **kwargs):
    context = {
        "text": "About us",
        "number": 123,
        "list": ["a", "b", 1, 2, 3]
    }
    return render(request, "about.html", context)

def social_view(request, *args, **kwargs):
    return render(request, "about.html", {})