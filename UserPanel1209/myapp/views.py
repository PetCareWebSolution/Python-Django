from django.shortcuts import render

# Create your views here.
def showhomepage(request):
    return render(request,'index.html')

def showcontact(request):
    return render(request,'contact.html')

def showproduct(request):
    return render(request,'product.html')