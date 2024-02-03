
from django.shortcuts import render, redirect, get_object_or_404
from .forms import OrderForm
from .models import Order

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'store/order_list.html', {'orders': orders})

def order_product(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('home')
    else:
        form = OrderForm()

    return render(request, 'store/order_form.html', {'form': form})
def home(request):
    context = {}
    return render(request, 'store/home.html', context)

def store(request):
    context = {}
    return render(request, 'store/store.html', context)

def cart(request):
    context = {}
    return render(request, 'store/cart.html', context)

def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)


def update_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('order_list')  
    else:
        form = OrderForm(instance=order)

    return render(request, 'store/update_order.html', {'form': form, 'order': order})

def delete_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    if request.method == 'POST':
        order.delete()
        return redirect('order_list') 
    
    return render(request, 'store/delete_order.html', {'order': order})


