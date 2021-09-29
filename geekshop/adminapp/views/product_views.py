from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from mainapp.models import Product, ProductCategory
from adminapp.forms import ProductEditForm


def products(request, pk):
    title = 'админка/продукты'

    category = get_object_or_404(ProductCategory, pk=pk)
    product_list = Product.objects.filter(category__pk=pk).order_by('name')
    content = {
        'title': title,
        'category': category,
        'objects': product_list
    }
    return render(request, 'adminapp/products.html', content)


def product_create(request):
    title = 'продукты/создание'

    if request.method == 'POST':
        product_form = ProductEditForm(request.POST, request.FILES)
        if product_form.is_valid():
            product_form.save()
            return HttpResponse(reverse('admin:products'))
    else:
        product_form = ProductEditForm()
    content = {'title': title, 'update_form': product_form}
    return render(request, 'adminapp/products.html')


def product_read(request, pk):
    title = 'админка/продукты'

    product = get_object_or_404(Product, pk=pk)
    content = {
        'title': title,
        'objects': product
    }
    return render(request, 'adminapp/products.html', content)


def product_update(request, pk):
    title = 'пользователи/создание'

    edit_product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        edit_form = ProductEditForm(request.POST, request.FILES, instance=edit_product)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponse(reverse('admin:users', args=[edit_product.pk]))
    else:
        edit_form = ProductEditForm(instance=edit_product)

    content = {'title': title, 'update_form': edit_form}
    return render(request, 'adminapp/products.html', content)


def product_delete(request, pk):
    title = 'пользователи/создание'

    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        product.is_active = False
        product.save()
        return HttpResponse(reverse('admin:products'))

    content = {'title': title, 'product_or_delete': product}
    return render(request, 'adminapp/products.html', content)
