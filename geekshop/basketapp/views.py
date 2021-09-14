
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Basket
from mainapp.models import Product
# Create your views here.


def basket(request):
    content = {}
    return render(request, 'basketapp/basket.html', content)


def basket_add(request, pk):
    product = get_object_or_404(Product, pk=pk)
    basket = Basket.objects.filter(user=request.user, pk=pk)

    if not basket:
        basket = Basket.objects.filter(user=request.user, product=product)

    basket[0].quantity += 1
    basket[0].save()
    return HttpResponseRedirect(reverse('main'))
#    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def basket_remove(request, pk):
    basket = Basket.objects.filter(user=request.user, pk=pk)
    basket[0].quantity -= 1
    basket[0].save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
