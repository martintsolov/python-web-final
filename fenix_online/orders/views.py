from django.shortcuts import render, redirect

from fenix_online.orders.forms import CreateOrderForm


def create_order(request):
    if request.method == 'POST':
        form = CreateOrderForm(request.POST)
        order = form.save(commit=False)
        order.owner = request.user
        order.save()
        return redirect('login')

    form = CreateOrderForm()

    context = {
        'form': form
    }
    return render(request, 'create_order.html', context)