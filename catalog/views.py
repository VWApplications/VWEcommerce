from django.shortcuts import render
from .models import Product, Category


def product_list(request):
  template = 'catalog/product_list.html'
  context = {
    'products': Product.objects.all()
  }
  return render(request, template, context)


def category(request, category_slug):
  template = 'catalog/category.html'
  category = Category.objects.get(slug=category_slug)
  context = {
    'category': category,
    'products': Product.objects.filter(category=category),
  }
  return render(request, template, context)


def product(request, product_slug):
  template = 'catalog/product.html'
  context = {
    'product': Product.objects.get(slug=product_slug),
  }
  return render(request, template, context)
