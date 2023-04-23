from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('register-parent/', registerParent, name='registerParent'),
    path('login-parent/', loginParent, name='loginParent'),
    path('add-child/', createChild, name='createChild'),
    path('dashboard-parent/', dashboardParent, name='dashboardParent'),
]