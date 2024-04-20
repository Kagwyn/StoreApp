from django.shortcuts import render
from .models import Product
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request, 'pages/index.html', {'products': products})

def show(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'pages/show.html', {'product': product})