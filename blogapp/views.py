from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def blogMain(request):
    return render(request, 'blogMain.html')