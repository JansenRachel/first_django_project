from django.shortcuts import render, redirect
from django.http import HttpResponse

def index(request):
    return HttpResponse('placeholder to later display a list of all blogs')

def create(request):
    return redirect('/')