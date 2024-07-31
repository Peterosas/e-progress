from django.urls import path
from .views import Login, Overview

urlpatterns = [
    path('login/', Login, name='s_login'),
    path('overview/', Overview, name='overview'),
]
