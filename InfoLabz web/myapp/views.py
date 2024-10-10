from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")

def contactpage(request):
    return render(request,"contact.html")

def abootpage(request):
    return render(request,"about.html")

def servicepage(request):
    return render(request,"services.html")