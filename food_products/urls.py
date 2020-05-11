from django.urls import path
from . import views

app_name = 'food_products'

urlpatterns = [
    path('', views.product_list, name='list'),
    path('<slug:slug>', views.product_detail, name='detail'),
]
