from django.urls import path
from . import views

urlpatterns = [
    path('cart', views.cart, name="cart"),
    path('update_item/', views.updateItem, name='updateItem'),
    path('checkout', views.checkout, name="checkout"),
    path('updateAddress/', views.updateAddress, name='updateAddress'),
    path('processOrder/', views.processOrder, name='processOrder')
]