from django.shortcuts import render, get_object_or_404
from mainapp.models import Product, ProductCategory


def main(request):
    title = 'Главная'
    products = Product.objects.all()
    content = {'title': title, 'products': products}
    return render(request, 'mainapp/index.html', content)


def products(request, pk=None):
    products = Product.objects.all()
    content = {'products': products}
    return render(request, 'mainapp/products_list.html', content)


def product(request, pk):
    product = Product.objects.filter(pk=pk)
    content = {'products': product}
    return render(request, 'mainapp/product_page.html', content)


def contact(request):
    return render(request, 'mainapp/contact.html')