from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'shop/index.html')

def products(request):
    pass

def product(request):
    pass

def like(request):
    pass

def cart(request):
    pass

def checkout(request):
    pass