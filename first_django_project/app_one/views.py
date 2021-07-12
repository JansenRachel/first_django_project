from django.shortcuts import redirect, render, HttpResponse

def index(request):
    return HttpResponse('placeholder to later display a list of all blogs')

def new(request):
    return HttpResponse('placeholder to display a new form to create a new blog')

def create(request):
    return redirect("/")

def show(requset, number):
    return HttpResponse(f"placeholser to display blog number: {number}")

def edit(request, number):
    return HttpResponse(f"placeholser to edit blog number: {number}")
    
def destroy(request, number):
    return redirect("/")
# Create your views here.
    