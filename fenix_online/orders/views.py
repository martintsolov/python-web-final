import datetime

from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseRedirect, HttpResponseNotFound
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages

from fenix_online.orders.forms import CreateOrderForm, ClientEditOrderForm
from fenix_online.orders.models import Order


@login_required
def create_order(request):
    if request.method == 'POST':
        form = CreateOrderForm(request.POST)
        order = form.save(commit=False)
        order.owner = request.user
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
def delete_order(request, pk):
    order_instance = Order.objects.get(pk=pk)
    active_user = request.user
    if order_instance.owner_id == request.user.id or active_user.is_staff:
        order_instance.delete()
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

