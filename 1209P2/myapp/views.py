from django.shortcuts import render

# Create your views here.
def showindex(request):
    return render(request,"index.html")

def showcontact(request):
    return render(request,"contact.html")