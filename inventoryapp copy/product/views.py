from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
# Create your views here.
from .models import Product
from .forms import ProductForm


def list_of_products(request):
    qs = Product.objects.all()
    context = {'product_list': qs}
    return render(request, 'product/product_list.html', context)


def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    context = {'product': product}
    return render(request, 'product/product_detail.html', context)


def product_from_user(request):

    context = {}

    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "product/product_from_user.html", context)


def update_product(request, id):
    context = {}

    obj = get_object_or_404(Product, id = id)

    form = ProductForm(request.POST or None, instance = obj)

    if form.is_valid():
        form.save()
        # return HttpResponseRedirect("/"+id)

    context["form"] = form

    return render(request, "product/update_product.html", context)
