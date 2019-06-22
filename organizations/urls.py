from django.urls import path, include
from organizations.views import credentials, register

app_name = 'organizations'
urlpatterns = [
    path('login', credentials.login, name='login'),
    path('logout', credentials.logout, name='logout'),
    path('register/', include([
        path('', register.main, name='register'),
        path('user', register.user, name='register_user'),
        path('organization', register.organization, name='register_organization'),
        path('address', register.address, name='register_address'),
    ])),
]