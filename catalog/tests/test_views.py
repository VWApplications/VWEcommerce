from django.test import TestCase, Client
from django.core.urlresolvers import reverse
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
    product_list = response.context['products']
    self.assertEquals(product_list.count(), 10)


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
    products = response.context['products']
    self.assertEquals(products.count(), 6)
    for product in products:
      self.assertEquals(product.category, response.context['category'])

  def test_devops_category_context(self):
    response = self.client.get(self.devops.get_absolute_url())
    self.assertTrue('category' in response.context)
    self.assertTrue('products' in response.context)
    products = response.context['products']
    self.assertEquals(products.count(), 7)
    for product in products:
      self.assertEquals(product.category, response.context['category'])
