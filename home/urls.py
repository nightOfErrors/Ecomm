from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('loginit', views.loginit, name="login"),
    path("logitout", views.logitout, name="logitout"),
    path("allproducts", views.allproducts, name="allproducts")
]
