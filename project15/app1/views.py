from django.shortcuts import render


# Create your views here.
def dad(request):
    return render(request,'dad.html')
def child1(request):
    return render(request,'child1.html') 


