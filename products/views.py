from django.shortcuts import render
from .models import *

# Create your views here.

def product(request, pk):

    productIn = Product.objects.get(id=pk)
    
    return render(request, 'product.html', {'productIn':productIn})