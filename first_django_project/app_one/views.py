from django.http import response
from django.shortcuts import render, HttpResponse

def index(request):
    return HttpResponse('placeholder to later display a list of all blogs')

def new(request):
    return HttpResponse('placeholder to display a new form to create a new blog')
# Create your views here.

from django.shortcuts import redirect

def
    redirect_view(request):
    response = redirect('/redirect-success/')
    return response