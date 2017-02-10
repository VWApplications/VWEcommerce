from django.test import TestCase, Client
from django.core.urlresolvers import reverse

class IndexViewTestCase(TestCase):

  def setUp(self):
    self.client = Client()

  def test_status_code_200(self):
    response = self.client.get(reverse('core:home'))
    self.assertEquals(response.status_code, 200)

  def test_template_used(self):
    response = self.client.get(reverse('core:home'))
    self.assertTemplateUsed(response, 'core/base.html')
    self.assertTemplateUsed(response, 'core/footer.html')
    self.assertTemplateUsed(response, 'core/home.html')
