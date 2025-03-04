from django.shortcuts import render

# Create your views here.
def mom(request):
    return render(request,'mom.html')
def cart(request):
    return render(request,'cart.html') 
