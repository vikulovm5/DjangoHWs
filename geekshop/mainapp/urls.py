from django.urls import path
from mainapp.views import products, contact, product

urlpatterns = [
    path('products/', products, name='products'),
    path('contact/', contact, name='contact'),
    path('product-page/<int:pk>/', product, name='product-page'),
]