from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from core.utils import generate_hash_key
from core.email import send_email_template
from .models import PasswordReset

User = get_user_model()


class UserAdminCreationForm(UserCreationForm):
  class Meta:
    model = User
    fields = ['username', 'email']


class UserAdminForm(forms.ModelForm):
  class Meta:
    model = User
    fields = ['username', 'email', 'name', 'is_active', 'is_staff']


class PasswordResetForm(forms.Form):
  email = forms.EmailField(label='E-mail')

  def clean_email(self):
    email = self.cleaned_data['email']
    if User.objects.filter(email=email).exists():
      return email
    raise forms.ValidationError('Nenhum usuário encontrado com esse email')

  def save(self):
    user = User.objects.get(email=self.cleaned_data['email'])
    key = generate_hash_key(user.username)
    reset_password = PasswordReset(user=user, key=key)
    reset_password.save()
    template = 'accounts/reset_password_email.html'
    subject = 'Solicitando nova senha'
    context = {'reset_password': reset_password}
    send_email_template(subject, template, context, [user.email])
