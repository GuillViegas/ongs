from django.urls import path, include
from organizations.views import credentials

app_name = 'organizations'
urlpatterns = [
    path('login', credentials.login, name='login'),
    path('logout', credentials.logout, name='logout'),
    path('register', credentials.register, name='register'),
]