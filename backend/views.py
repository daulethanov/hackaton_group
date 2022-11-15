from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
import random
from .forms import *
from django.urls import reverse_lazy
from django.views.generic import CreateView


def home(request):
    return render(request, 'home.html')


# class RegisterUser(CreateView):
#     form_class = RegisterUserForm
#     template_name = 'register.html'
#     success_url = reverse_lazy('login')
#
#
#     def form_valid(self, form):
#
#         user = form.save()
#         login(self.request, user)
#         teams = Team.objects.filter(users_group__id=1)
#         teams.user_permissions.add()
#         # if User.is_authenticated == True:
#
#         return redirect('home')






class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('account')


def logout_user(request):
    logout(request)
    return redirect('home')


def register(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = form.cleaned_data['group']
            group.user_set.add(user)
             #group.user_set.add(user.id) #if data in user is not of int, then use id with that to get primary int value. Else no need
            return redirect('login')
    else:
        form = RegisterUserForm()
    return render(request, 'register.html', {'form':form})
