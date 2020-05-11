from django.http import HttpResponse
from django.shortcuts import render, redirect
from food_products.models import ProductDetail

def about(request):
    return render(request, 'about.html')

def homepage(request):
    categories = ProductDetail.objects.all().order_by('-created_at')
    return render(request, 'homepage.html', {'categories': categories})