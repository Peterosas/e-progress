from django.shortcuts import render

def Login(request):
    return render(request, 'login.html')

def DashboardOverview(request):
    return render(request, 'dashboard_overview.html')

def PrintResults(request):
    return render(request, 'print_results.html')

def MyProfile(request):
    return render(request, 'profile.html')

def MyCourses(request):
    return render(request, 'courses.html')
