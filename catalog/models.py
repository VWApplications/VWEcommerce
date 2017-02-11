from django.db import models
from django.core.urlresolvers import reverse


class Category(models.Model):
  name = models.CharField('Nome', max_length=100)
  slug = models.SlugField('Identificador', max_length=100)
  created_at = models.DateTimeField('Criado em', auto_now_add=True)
  updated_at = models.DateTimeField('Modificado em', auto_now=True)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('catalog:category', kwargs={'category_slug': self.slug})

  class Meta:
    verbose_name = 'Categoria'
    verbose_name_plural = 'Categorias'
    ordering = ['name']


class Product(models.Model):
  name = models.CharField('Nome', max_length=100)
  slug = models.SlugField('Identificador', max_length=100)
  description = models.TextField('Descrição', blank=True)
  price = models.DecimalField('Preço', decimal_places=2, max_digits=10)
  category = models.ForeignKey(Category, verbose_name="Categoria", related_name="products")
  created_at = models.DateTimeField('Criado em', auto_now_add=True)
  updated_at = models.DateTimeField('Modificado em', auto_now=True)

  def __str__(self):
    return self.name

  def get_absolute_url(self):
    return reverse('catalog:product', kwargs={'product_slug': self.slug})

  class Meta:
    verbose_name = 'Produto'
    verbose_name_plural = 'Produtos'
    ordering = ['name']

