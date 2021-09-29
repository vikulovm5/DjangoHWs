from django.urls import path
import mainapp.views as mainapp

import geekshop.adminapp.views.product_views

app_name = 'mainapp'

urlpatterns = [
    path('', geekshop.adminapp.views.product_views.products, name='index'),
    path('category/<int:pk>/', geekshop.adminapp.views.product_views.products, name='category'),
    path('product/<int:pk>/', mainapp.product, name='product'),
]
