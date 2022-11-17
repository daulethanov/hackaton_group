from django.urls import path
from .views import *

urlpatterns = [
    path('', GroupsList.as_view(), name='home'),
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', register, name='register'),
    path('logout/', logout_user, name='logout'),
    path('group_detail/<int:pk>/', GroupDetail.as_view(), name='group_detail'),
    path('group_detail/<int:pk>/leave/', leave, name='leave'),
]