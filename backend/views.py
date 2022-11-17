from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import Group
from .forms import *
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView


def leave(request, pk):
    if request.method == 'POST':
        group = get_object_or_404(Group, pk=pk)
        if request.user in group.user_set.all():
            group.user_set.remove(request.user)
            group.save()
            return redirect('home')
        else:
            return render(request, 'groups_detail.html')
    return render(request, 'groups_detail.html')

def home(request):
    return render(request, 'home.html')


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'

    def get_success_url(self):
        return reverse_lazy('home')


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
            return redirect('login')
    else:
        form = RegisterUserForm()
    return render(request, 'register.html', {'form':form})


class GroupsList(ListView):
    model = Group
    template_name = 'home.html'
    context_object_name = 'groups'

    def get_context_data(self, **kwargs):
        context = super(GroupsList, self).get_context_data(**kwargs)
        context['groups'] = Group.objects.all()
        return context


class GroupDetail(DetailView):
    model = Group
    context_object_name = 'group_detail'
    template_name = 'groups_detail.html'


def group_join(request):
    if request.method == 'POST':
        form = GroupForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = form.cleaned_data['group']
            group.user_set.add(user)
            return redirect('group_detail')
        else:
            form = GroupForm()
        return render(request, 'home.html', {'form': form})







