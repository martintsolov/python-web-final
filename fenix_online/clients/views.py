from django import forms
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import transaction
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from fenix_online.clients.forms import UserForm, ClientForm, EditUserForm
from fenix_online.clients.models import Client


def client_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
            else:
                messages.error(request, 'User is not active.')
                return HttpResponseRedirect(reverse('login'))
        else:
            messages.error(request, 'Invalid login credentials. Please try again!')
            return HttpResponseRedirect(reverse('login'))
    else:
        return render(request, 'login.html', {})


def client_register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        client_form = ClientForm(data=request.POST)
        if user_form.is_valid() and client_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            client = client_form.save(commit=False)
            client.user = user
            client.save()
            return redirect('login')
        else:
            print(user_form.errors, client_form.errors)
    else:
        user_form = UserForm()
        client_form = ClientForm()
        return render(request, 'register.html', {'user_form': user_form,
                                             'client_form': client_form,
                                             'registered': registered})


@login_required
def home(request):
    current_user = request.user
    current_client = Client(user_id=current_user.id)
    context = {
        'client': current_client,
        'user': current_user,
    }

    return render(request, 'home.html', context)


@login_required
def client_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


@login_required
def client_profile(request):
    current_user = request.user
    client = Client.objects.get(user_id=current_user.id)

    context = {
        'user': current_user,
        'client': client,
    }

    return render(request, 'client_profile.html', context)


@login_required
@transaction.atomic
def edit_client_profile(request):
    if request.method == 'POST':
        user_form = EditUserForm(request.POST, instance=request.user)
        client_form = ClientForm(request.POST, instance=Client.objects.get(user_id=request.user.id))
        if user_form.is_valid() and client_form.is_valid():
            user_form.save()
            client_form.save()
            messages.success(request, message='Your profile was updated!')
            return redirect('client profile')
        else:
            messages.error(request, message='Please check you entries!')
    else:
        user_form = EditUserForm(instance=request.user)
        client_form = ClientForm(instance=Client.objects.get(user_id=request.user.id))
    return render(request, 'edit_client_profile.html', {'user_form': user_form, 'client_form': client_form})


@login_required
@transaction.atomic
def delete_client_profile(request):
    user = request.user
    client = Client.objects.get(user_id=request.user.id)
    user.delete()
    client.delete()
    return HttpResponseRedirect('../login')


@login_required
@staff_member_required
def admin_list_clients(request):
    users = User.objects.all()
    clients = Client.objects.all().order_by('company_name')

    context = {
        'users': users,
        'clients': clients,
    }

    return render(request, 'admin_clients_list.html', context)


@login_required
@transaction.atomic
@staff_member_required
def admin_edit_client_profile(request, pk):
    user = User.objects.get(id=pk)
    client = Client.objects.get(user_id=pk)

    if request.method == 'POST':
        user_form = EditUserForm(request.POST, instance=user)
        client_form = ClientForm(request.POST, instance=client)
        if user_form.is_valid() and client_form.is_valid():
            user_form.save()
            client_form.save()
            messages.success(request, message='Client profile was updated!')
            return redirect('admin list clients')
        else:
            messages.error(request, message='Please check you entries!')
    else:
        user_form = EditUserForm(instance=user)
        client_form = ClientForm(instance=client)
    return render(request, 'admin_edit_client.html', {
        'user_form': user_form,
        'client_form': client_form,
        'user': user,
        'client': client,})


@login_required
@transaction.atomic
@staff_member_required
def admin_delete_client(request, pk):
    user = User.objects.get(id=pk)
    client = Client.objects.get(user_id=pk)
    user.delete()
    client.delete()
    return HttpResponseRedirect('../list_clients')