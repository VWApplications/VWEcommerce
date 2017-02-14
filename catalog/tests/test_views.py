from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator
from catalog.models import Product, Category
from model_mommy import mommy


class ProductListTestCase(TestCase):

  def setUp(self):
    self.url = reverse('catalog:product_list')
    mommy.make(Product, _quantity=10)
    self.client = Client()

  def tearDown(self):
    Product.objects.all().delete()

  def test_status_code_200(self):
    response = self.client.get(self.url)
    self.assertEquals(response.status_code, 200)
    self.assertTemplateUsed(response, 'catalog/product_list.html')
    self.assertTemplateUsed(response, 'catalog/list.html')

  def test_context(self):
    response = self.client.get(self.url)
    self.assertTrue('products' in response.context)
    self.assertTrue('paginator' in response.context)
    self.assertTrue('page_obj' in response.context)

  def test_pagination(self):
    response = self.client.get(self.url)
    paginator = response.context['paginator']
    products = response.context['products']
    self.assertEquals(paginator.count, 10)
    self.assertEquals(paginator.per_page, 2)
    self.assertEquals(paginator.num_pages, 5)
    self.assertEquals(products.count(), 2)

  def test_page_not_found(self):
    response = self.client.get('{0}?page=6'.format(self.url))
    self.assertEquals(response.status_code, 404)


class CategoryTestCase(TestCase):

  def setUp(self):
    self.design = mommy.make(Category, name="design")
    self.devops = mommy.make(Category, name="devops")
    mommy.make(Product, category=self.design, _quantity=6)
    mommy.make(Product, category=self.devops, _quantity=7)
    self.client = Client()

  def tearDown(self):
    Product.objects.all().delete()
    Category.objects.all().delete()

  def test_status_ok(self):
    response = self.client.get(self.design.get_absolute_url())
    self.assertEquals(response.status_code, 200)
    self.assertTemplateUsed(response, 'catalog/category.html')
    self.assertTemplateUsed(response, 'catalog/list.html')

  def test_design_category_context(self):
    response = self.client.get(self.design.get_absolute_url())
    self.assertTrue('category' in response.context)
    self.assertTrue('products' in response.context)
    self.assertTrue('paginator' in response.context)
    self.assertTrue('page_obj' in response.context)

  def test_design_category_pagination(self):
    response = self.client.get(self.design.get_absolute_url())
    paginator = response.context['paginator']
    products = response.context['products']
    self.assertEquals(paginator.count, 6)
    self.assertEquals(paginator.per_page, 2)
    self.assertEquals(paginator.num_pages, 3)
    self.assertEquals(products.count(), 2)
    for product in products:
      self.assertEquals(product.category, response.context['category'])

  def test_devops_category_context(self):
    response = self.client.get(self.devops.get_absolute_url())
    self.assertTrue('category' in response.context)
    self.assertTrue('products' in response.context)
    self.assertTrue('paginator' in response.context)
    self.assertTrue('page_obj' in response.context)

  def test_devops_category_pagination(self):
    response = self.client.get(self.devops.get_absolute_url())
    paginator = response.context['paginator']
    products = response.context['products']
    self.assertEquals(paginator.count, 7)
    self.assertEquals(paginator.per_page, 2)
    self.assertEquals(paginator.num_pages, 4)
    self.assertEquals(products.count(), 2)
    for product in products:
      self.assertEquals(product.category, response.context['category'])


class ProductViewTestCase(TestCase):

  def setUp(self):
    self.client = Client()
    self.product = mommy.make(Product, name='Curso de Python')

  def test_status_ok(self):
    response = self.client.get(self.product.get_absolute_url())
    self.assertEquals(response.status_code, 200)
    self.assertTemplateUsed(response, 'catalog/product.html')

  def test_context(self):
    response = self.client.get(self.product.get_absolute_url())
    self.assertTrue('product' in response.context)
    product = response.context['product']
    self.assertEquals(product.name, response.context['product'].name)
