from django.shortcuts import render, get_object_or_404
from mainapp.models import Product, ProductCategory

from basketapp.models import Basket


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


def count(request, pk):
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)

    if pk:
        if pk == '0':
            products = Product.objects.all().order_by('price')
            category = {'name': 'все'}
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(category__pk=pk).order_by('price')

        content = {
            'title': title,
            'links_menu': links_menu,
            'category': category,
            'products': products,
            'basket': basket,
        }

        return render(request, 'mainapp/products_list.html', content)