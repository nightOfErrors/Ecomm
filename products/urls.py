from django import urls
from django.urls import path
from . import views

urlpatterns = [
    path('product/<str:pk>/', views.product, name="product")
]
