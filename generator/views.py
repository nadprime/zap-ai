from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def landing_page(request):
    return render(request, 'landing_page.html')