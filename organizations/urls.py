from django.urls import path, include
from organizations.views import credentials

app_name = 'organizations'
urlpatterns = [
    path('login', credentials.login, name='login'),
    path('logout', credentials.logout, name='logout'),
    path('register/', include([
        path('', credentials.register, name='register'),
        path('user', credentials.registerUser, name='register_user'),
        path('organization', credentials.registerOrganization, name='register_organization'),
    ])),
]