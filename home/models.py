from django.db import models
from products.models import *
from django.contrib.auth.models import User

# Create your models here.

class Customer(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name


class Order(models.Model):

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    dateOrdered = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    completed = models.BooleanField(default=False, null=True, blank=True)
    OrderId =  models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total


class OrderItem(models.Model):

    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)    
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    quantity = models.IntegerField(default=0 , null=True, blank=True)

    def __str__(self):
        return str(self.product)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


class ShippingAddress(models.Model):

    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=True, blank=True)
    address = models.TextField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    zipcode = models.IntegerField(null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.address

   



