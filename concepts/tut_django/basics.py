"""
django-admin startproject myproject
cd myproject
python manage.py startapp myapp
"""
### Models 
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# python manage.py makemigrations
# python manage.py migrate

### Admin Interface
from django.contrib import admin
from .models import Product

admin.site.register(Product)

## Function Based Views 
from django.shortcuts import render
from .models import Product

def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

### Class Based Views 
from django.views.generic import ListView
from .models import Product

class ProductListView(ListView):
    model = Product
    template_name = 'product_list.html'


## Urls 
from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_list, name='product_list'),  # FBV
    path('products_cbv/', views.ProductListView.as_view(), name='product_list_cbv'),  # CBV
]
#### Templates 
"""
<!DOCTYPE html>
<html>
<head>
    <title>Product List</title>
</head>
<body>
    <h1>Products</h1>
    <ul>
    {% for product in products %}
        <li>{{ product.name }} - ${{ product.price }}</li>
    {% endfor %}
    </ul>
</body>
</html>

"""

#### Forms
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price']




########### Form Data 
from django.shortcuts import render, redirect
from .forms import ProductForm

def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm()
    return render(request, 'product_form.html', {'form': form})


############## Middleware
class CustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response
    
### Django REST Framework (DRF)
# Serializers
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

# Viewset
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

## Urls 
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = router.urls


###### Testing 

from django.test import TestCase
from .models import Product

class ProductModelTest(TestCase):
    def setUp(self):
        Product.objects.create(name='Test Product', price='10.00')

    def test_product_creation(self):
        product = Product.objects.get(name='Test Product')
        self.assertEqual(product.price, 10.00)

######### Authentication 
from django.contrib.auth import login, logout
from django.shortcuts import redirect

def user_login(request):
    if request.method == 'POST':
        # authenticate user and login
        return redirect('home')
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    return redirect('login')

########### Signals 
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Product

@receiver(post_save, sender=Product)
def product_saved(sender, instance, **kwargs):
    print(f'{instance.name} has been saved!')

########## Deployment 
pip install gunicorn
gunicorn myproject.wsgi:application --bind 0.0.0.0:8000


## Key Concepts to discuss 
"""
ORM best practices and performance tuning.
Class-Based Views (CBVs) vs Function-Based Views (FBVs).
Middleware for handling custom logic.
API Development with Django REST Framework.
Authentication & Authorization (JWT, OAuth).
Asynchronous Tasks using Celery with Django.
Testing Strategies (Unit, Integration, End-to-End).
Security: CSRF, XSS, SQL Injection prevention.
"""



