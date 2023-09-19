from django.shortcuts import render
from .models import Transaction
from .forms import UserInfoForm
from store.models import Cart, Product, Order
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.template.loader import render_to_string


def makeOrder(request):
    if request.method != 'POST':
        return redirect('store.checksout')

    form = UserInfoForm(request.POST)

    if form .is_valid():
        cart = Cart.objects.filter(session=request.session.session_key).last()
        products = Product.objects.filter(pk__in=cart.items)

        total = 0

        for item in products:
            total += item.price

        if total <= 0:
            return redirect('store.cart')

        order = Order.objects.create(customer=form.cleaned_data, total=total)

        for product in products:
            order.orderproduct_set.create(
                product_id=product.id, price=product.price)

        send_order_email(order, products)
        cart.delete()
        return redirect('store.checkout_complate')
    else:
        return redirect('store.checkout')


def makeOrder(request):
    form = UserInfoForm(request.POST)

    if form .is_valid():
        cart = Cart.objects.filter(session=request.session.session_key).last()
        products = Product.objects.filter(pk__in=cart.items)

        total = 0

        for item in products:
            total += item.price

        if total <= 0:
            return None

        order = Transaction.objects.create(customer=form.cleaned_data, total=total)

        for product in products:
            order.orderproduct_set.create(
                product_id=product.id, price=product.price)

        send_order_email(order, products)
        cart.delete()
        return redirect('store.checkout_complate')
    else:
        return redirect('store.checkout')


def send_order_email(order, products):
    msg_html = render_to_string('emails/order.html', {
        'order': order,
        'products': products,
    })
    send_mail(
        subject='New Order',
        html_message=msg_html,
        message=msg_html,
        from_email='norplay@example.com',
        recipient_list=['customer@example.com']
    )
