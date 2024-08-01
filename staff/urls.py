from django.urls import path
from .views import Login, DashboardOverview, PrintResults

urlpatterns = [
    path('login/', Login, name='s_login'),
    path('dashboard/overview/', DashboardOverview, name='dashboard_overview'),
    path('dashboard/results/', PrintResults, name='print_results'),
]
