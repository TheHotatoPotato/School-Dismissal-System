from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('register-school/', registerSchool, name='registerSchool'),
    path('login-school/', loginSchool, name='loginSchool'),
    path('logout-school/', logoutSchool, name='logoutSchool'),
    path('school-settings/', schoolSettings, name='schoolSettings'),
    path('dashboard-school/', dashboardSchool, name='dashboardSchool'),
    path('child-requests/', childRequests, name='childRequests'),
    path('approve-child/<str:pk>/', approveChild, name='approveChild'),
]