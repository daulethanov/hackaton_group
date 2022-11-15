from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('login', LoginUser.as_view(), name='login'),
    path('register', register, name='register'),
    path('logout', logout_user, name='logout'),
]