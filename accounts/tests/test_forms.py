from django.test import TestCase, Client
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model
from model_mommy import mommy
from django.conf import settings


User = get_user_model()


class RegisterViewTestCase(TestCase):

  def setUp(self):
    self.client = Client()
    self.register_url = reverse('accounts:register')

  def test_register_ok(self):
    data = {'username': 'fulano', 'email': 'fulano@gmail.com', 'password1': 'django1234', 'password2': 'django1234'}
    response = self.client.post(self.register_url, data)
    profile_url = reverse('accounts:profile')
    self.assertEquals(response.status_code, 302)
    self.assertRedirects(response, profile_url, target_status_code=302)
    self.assertEquals(User.objects.count(), 1)

  def test_register_error(self):
    data = {'username': 'fulano', 'password1': 'django1234', 'password2': 'django1234'}
    response = self.client.post(self.register_url, data)
    self.assertFormError(response, 'form', 'email', 'Este campo é obrigatório.')


class UpdateUserTestCase(TestCase):

  def setUp(self):
    self.client = Client()
    self.update_url = reverse('accounts:edit')
    self.user = mommy.prepare(settings.AUTH_USER_MODEL)
    self.user.set_password('123')
    self.user.save()

  def tearDown(self):
    self.user.delete()

  # def test_update_user_ok(self):
  #   data = {'name': 'teste', 'email': 'test@test.com'}
  #   response = self.client.get(self.update_url)
  #   self.assertEquals(response.status_code, 302)
  #   self.client.login(username=self.user.username, password='123')
  #   response = self.client.get(self.update_url)
  #   self.assertEquals(response.status_code, 200)
  #   response = self.client.post(self.update_url, data)
  #   profile_url = reverse('accounts:profile')
  #   self.assertRedirects(response, profile_url)
  #   self.user.refresh_from_db()
  #   self.assertEquals(self.user.email, data['email'])
  #   self.assertEquals(self.user.name, data['name'])

  def test_update_user_error(self):
    data = {'name': 'teste', 'email': ''}
    self.client.login(username=self.user.username, password='123')
    response = self.client.post(self.update_url, data)
    self.assertFormError(response, 'form', 'email', 'Este campo é obrigatório.')


class UpdatePasswordTestCase(TestCase):

  def setUp(self):
    self.client = Client()
    self.update_password_url = reverse('accounts:edit_password')
    self.user = mommy.prepare(settings.AUTH_USER_MODEL)
    self.user.set_password('123')
    self.user.save()

  def tearDown(self):
    self.user.delete()

  def test_update_password_ok(self):
    data = {'old_password': '123', 'new_password1': 'django1234', 'new_password2': 'django1234'}
    self.client.login(username=self.user.username, password='123')
    response = self.client.post(self.update_password_url, data)
    self.user.refresh_from_db()
    self.assertTrue(self.user.check_password('django1234'))
