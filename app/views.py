from django.shortcuts import render

# Create your views here.
def cdn(request):
    return render(request,'cdn.html')
def new(request):
    return render(request,'new.html')