from django.shortcuts import render
from .models import Pages
# Create your views here.


def home(request):
    pages = Pages.objects.all()
    return render(request, 'pages/home.html', {'pages': pages})

def about(request):
    return render(request, 'pages/about.html')
