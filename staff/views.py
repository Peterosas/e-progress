from django.shortcuts import render

def Login(request):
    return render(request, 'login.html')

def Overview(request):
    return render(request, 'dashboard.html')
