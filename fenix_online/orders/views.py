import datetime

from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages

from fenix_online.clients.models import Client
from fenix_online.orders.forms import CreateOrderForm, ClientEditOrderForm, AdminEditOrderForm
from fenix_online.orders.models import Order


@login_required
def create_order(request):
    if request.method == 'POST':
        form = CreateOrderForm(request.POST)
        order = form.save(commit=False)
        order.owner = request.user
        order.client = Client.objects.get(user_id=request.user.id)
        order.save()
        return redirect('list orders')

    form = CreateOrderForm()

    context = {
        'form': form
    }
    return render(request, 'create_order.html', context)


@login_required
def list_orders(request):
    current_user_id = request.user.id
    orders = Order.objects.filter(owner=current_user_id).order_by('-created_at')

    context = {
        'orders': orders
    }

    return render(request, 'orders_list.html', context)


@login_required
@staff_member_required
def admin_list_orders(request):
    orders = Order.objects.all().order_by('wanted_date')
    context = {
        'orders': orders,
    }

    return render(request, 'admin_orders_list.html', context)


@login_required
@staff_member_required
def admin_list_received_orders(request):
    orders = Order.objects.filter(status='Received').order_by('wanted_date')
    context = {
        'orders': orders,
    }
    return render(request, 'admin_received_orders_list.html', context)


@login_required
@staff_member_required
def admin_list_scheduled_orders(request):
    orders = Order.objects.filter(status='Scheduled').order_by('wanted_date')
    context = {
        'orders': orders,
    }
    return render(request, 'admin_scheduled_orders_list.html', context)


@login_required
@staff_member_required
def admin_list_delivered_orders(request):
    orders = Order.objects.filter(status='Delivered').order_by('wanted_date')
    context = {
        'orders': orders,
    }
    return render(request, 'admin_delivered_orders_list.html', context)


@login_required
@staff_member_required
def admin_list_full_orders(request):
    orders = Order.objects.filter(status='Full').order_by('wanted_date')
    context = {
        'orders': orders,
    }
    return render(request, 'admin_full_orders_list.html', context)


@login_required
@staff_member_required
def admin_list_picked_orders(request):
    orders = Order.objects.filter(status='Picked-up').order_by('wanted_date')
    context = {
        'orders': orders,
    }
    return render(request, 'admin_picked_orders_list.html', context)


@login_required
def client_edit_order(request, pk):
    order_instance = Order.objects.get(pk=pk)
    active_user = request.user
    if order_instance.owner_id == request.user.id or active_user.is_staff:
        if request.method == 'POST':
            form = ClientEditOrderForm(request.POST, instance=order_instance)
            form.save()
            return redirect('list orders')
        else:
            form = ClientEditOrderForm(instance=order_instance)
            context = {
                'form': form,
                'order': order_instance,
            }
            return render(request, 'client_edit_order.html', context)
    else:
        raise PermissionDenied


@login_required
@staff_member_required
def admin_edit_order(request, pk):
    order_instance = Order.objects.get(pk=pk)
    if request.method == 'POST':
        form = AdminEditOrderForm(request.POST, instance=order_instance)
        if form.is_valid():
            form.save()
            return redirect('admin list orders')
        else:
            print(form.errors)
    else:
        form = AdminEditOrderForm(instance=order_instance)
        context = {
            'form': form,
            'order': order_instance,
        }
        return render(request, 'admin_edit_order.html', context)


@login_required
def delete_order(request, pk):
    order_instance = Order.objects.get(pk=pk)
    active_user = request.user
    if order_instance.owner_id == request.user.id or active_user.is_staff:
        order_instance.delete()
        if active_user.is_staff:
            return redirect('admin list orders')
        return redirect('list orders')
    else:
        raise PermissionDenied


@login_required
def mark_order_as_full(request, pk):
    order = Order.objects.get(pk=pk)
    order.status = 'Full'
    order.save()
    return HttpResponseRedirect(reverse('list orders'))


@login_required
def dump_and_return(request, pk):
    order_instance = Order.objects.get(pk=pk)
    active_user = request.user
    if order_instance.owner_id == request.user.id or active_user.is_staff:
        mark_order_as_full(request, pk)
        return_order = Order.objects.create(
            status='Delivered',
            container_size=Order.objects.get(pk=pk).container_size,
            wanted_date=datetime.date.today(),
            container_id=Order.objects.get(pk=pk).container_id,
            owner_id=active_user.id
        )
        return_order.save()
        return HttpResponseRedirect(reverse('list orders'))
    else:
        return HttpResponseNotFound('You cannot access this order')

