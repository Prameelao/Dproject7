from django.shortcuts import render

# Create your views here

def registration(request):
    return render(request,'registration.html')
def login(request):
    return render(request,'login.html')
