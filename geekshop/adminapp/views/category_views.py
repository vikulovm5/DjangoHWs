from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from mainapp.models import ProductCategory
from adminapp.forms import ProductCategoryEditForm


def categories(request):
    title = 'админка/категории'

    category_list = ProductCategory.objects.all()
    content = {
        'title': title,
        'objects': category_list
    }
    return render(request, 'adminapp/categories.html', content)


def category_create(request):
    title = 'категориии/создание'

    if request.method == 'POST':
        category_form = ProductCategoryEditForm(request.POST, request.FILES)
        if category_form.is_valid():
            category_form.save()
            return HttpResponse(reverse('admin:users'))
    else:
        category_form = ProductCategoryEditForm()
    content = {'title': title, 'update_form': category_form}
    return render(request, 'adminapp/categories.html')


def category_update(request, pk):
    title = 'категориии/создание'

    edit_category = get_object_or_404(ProductCategory, pk=pk)
    if request.method == 'POST':
        edit_form = ProductCategoryEditForm(request.POST, request.FILES, instance=edit_category)
        if edit_form.is_valid():
            edit_form.save()
            return HttpResponse(reverse('admin:categories', args=[edit_category.pk]))
    else:
        edit_form = ProductCategoryEditForm(instance=edit_category)

    content = {'title': title, 'update_form': edit_form}
    return render(request, 'adminapp/categories.html', content)


def category_delete(request, pk):
    title = 'категориии/создание'

    category = get_object_or_404(ProductCategory, pk=pk)
    if request.method == 'POST':
        category.is_active = False
        category.save()
        return HttpResponse(reverse('admin:categories'))

    content = {'title': title, 'category_or_delete': category}
    return render(request, 'adminapp/categories.html', content)
