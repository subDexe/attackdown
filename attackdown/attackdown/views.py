from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def index(request):
	return render(request, 'logado.html')