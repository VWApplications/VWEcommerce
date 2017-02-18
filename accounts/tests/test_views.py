from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from model_mommy import mommy
from django.conf import settings


class LoginViewTestCase(TestCase):

  def setUp(self):
    self.client = Client()
    self.login_url = reverse('accounts:login')
    self.user = mommy.prepare(settings.AUTH_USER_MODEL)
    self.user.set_password('123')
    self.user.save()

  def tearDown(self):
    self.user.delete()

  def test_login_ok(self):
    response = self.client.get(self.login_url)
    self.assertEquals(response.status_code, 200)
    self.assertTemplateUsed(response, 'accounts/login.html')
    self.assertTrue(not response.wsgi_request.user.is_authenticated())
    data = {'username': self.user.username, 'password': '123'}
    response = self.client.post(self.login_url, data)
    redirect_url = reverse(settings.LOGIN_REDIRECT_URL)
    self.assertEquals(response.status_code, 302)
    self.assertRedirects(response, redirect_url)
    self.assertTrue(response.wsgi_request.user.is_authenticated())


  def test_login_error(self):
    data = {'username': self.user.username, 'password': '1234'}
    response = self.client.post(self.login_url, data)
    self.assertEquals(response.status_code, 200)
    self.assertTemplateUsed(response, 'accounts/login.html')
    error_msg = ('Por favor, entre com um Nome de Usuário  e senha corretos.'
                ' Note que ambos os campos diferenciam maiúsculas e minúsculas.')
    self.assertFormError(response, 'form', None, error_msg)
