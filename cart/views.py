from django.shortcuts import redirect, render
from django.http.response import JsonResponse
from django.contrib.auth.models import User
from home.models import *
from .forms import *
import json

# Create your views here.


def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, completed=False)
        items = order.orderitem_set.all()
        # print(items)
        total = 0
        for item in items:
            i = item.product.price * item.quantity
            total = total + i
    else: 
        return redirect('/')

    return render(request, "cart.html", {'items': items, 'total': total})


def updateItem(request):

    if request.method == "POST":
        data = json.loads(request.body)
        proKey = int(data['productId'])
        product = Product.objects.get(id=proKey)

        customer = request.user.customer
        order, created = Order.objects.get_or_create(
            customer=customer, completed=False)

        orderItem, created = OrderItem.objects.get_or_create(
            order=order, product=product)
        orderItem.quantity = orderItem.quantity + 1

        orderItem.save()

        items = order.orderitem_set.all()

        quantity = 0
        for item in items:
            quantity = quantity + item.quantity

        info = str(quantity)

    return JsonResponse(info, safe=False)


def checkout(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, completed=False)
        items = order.orderitem_set.all()
        # print(items)
        total = 0
        for item in items:
            i = item.product.price * item.quantity
            total = total + i        

    return render(request, "checkout.html", {'items': items, 'total': total, 'order':order})


def updateAddress(request):

    if request.method == "POST":
        data = json.loads(request.body)
        # print(data['city'])
    

        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, completed=False)   
        shippingAddress, created = ShippingAddress.objects.get_or_create(order=order) 
        shippingAddress.address = data['address']
        shippingAddress.zipcode = int(data['zipcode'])
        shippingAddress.city = data['city']
        shippingAddress.state = data['state']
        shippingAddress.country = data['country']

        shippingAddress.save()

        address = ShippingAddress.objects.get(order=order)
        thowableData = {
            'address' : str(address.address),
            'zipcode' : str(address.zipcode),
            'city' : str(address.city),
            'state' : str(address.state),
            'country' : str(address.country)
        }

    return JsonResponse(thowableData, safe=False)


def processOrder(request):

    customer = request.user.customer
    order, created = Order.objects.get_or_create(customer=customer, completed=False)  

    if request.method == "POST":
        data = json.loads(request.body)

        
        order.completed = True
        order.save()

    return JsonResponse("moved back", safe=False)


