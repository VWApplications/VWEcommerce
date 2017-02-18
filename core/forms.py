from django import forms
from core.email import send_email_template
from django.conf import settings


class ContactForm(forms.Form):
  name = forms.CharField(label='Nome')
  email = forms.EmailField(label='E-mail')
  message = forms.CharField(label='Mensagem', widget=forms.Textarea())

  def send_email(self, user):
    subject = 'Contato do VWE-Commerce: %s' % user
    template = 'core/contact_email.html'
    context = {
      'name': self.cleaned_data['name'],
      'email': self.cleaned_data['email'],
      'message': self.cleaned_data['message']
    }
    send_email_template(subject, template, context, [settings.CONTACT_EMAIL], context['email'])
