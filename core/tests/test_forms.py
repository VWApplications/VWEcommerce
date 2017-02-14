from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.core import mail


class ContactTestCase(TestCase):

  def setUp(self):
    self.client = Client()
    self.url = reverse('core:home')

  def test_form_errors(self):
    data = {'name': '', 'message': '', 'email': ''}
    response = self.client.post(self.url, data)
    self.assertFormError(response, 'form', 'name', 'Este campo é obrigatório.' )
    self.assertFormError(response, 'form', 'email', 'Este campo é obrigatório.' )
    self.assertFormError(response, 'form', 'message', 'Este campo é obrigatório.' )

  def test_form_correct(self):
    data = {'name': 'Pedro Calile', 'message': 'Mensagem de teste', 'email': 'pedro@gmail.com'}
    response = self.client.post(self.url, data)
    self.assertEquals(len(mail.outbox), 1)
    self.assertEquals(mail.outbox[0].subject, 'Contato do spoon E-Commerce')

