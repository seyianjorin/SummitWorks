from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Product
from .forms import ProductForm


class ProductList(ListView):
    queryset = Product.objects.all()
    model = Product
    templates = 'product/product_list.html'
    context_object_name = 'product_list'


class ProductDetail(DetailView):
    model = Product
    template_name = 'product/product_detail.html'
    context_object_name = 'product'


class CreateProduct(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/product_from_user.html'
    context_object_name = 'form'
    success_url = reverse_lazy('product_list')


class UpdateProduct(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'product/update_product.html'
    context_object_name = 'form'
    success_url = reverse_lazy('product_list')


class DeleteProduct(DeleteView):
    model = Product
    template_name = 'product/delete_product.html'
    success_url = reverse_lazy('product_list')


