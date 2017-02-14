from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.views.generic import ListView


class ProductListView(ListView):
  model = Product
  template_name = 'catalog/product_list.html'
  context_object_name = 'products'
  paginate_by = 2


class CategoryListView(ListView):
  template_name = 'catalog/category.html'
  context_object_name = 'products'
  paginate_by = 2

  def get_queryset(self):
    products = Product.objects.filter(category__slug=self.kwargs['category_slug'])
    return products

  def get_context_data(self, **kwargs):
    context = super(CategoryListView, self).get_context_data(**kwargs)
    context['category'] = get_object_or_404(Category, slug=self.kwargs['category_slug'])
    return context


def product(request, product_slug):
  template = 'catalog/product.html'
  context = {
    'product': Product.objects.get(slug=product_slug),
  }
  return render(request, template, context)
