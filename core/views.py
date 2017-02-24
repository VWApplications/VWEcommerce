from django.shortcuts import render
from .forms import ContactForm
from django.contrib import messages


def home(request):
  template = 'core/home.html'
  form = ContactForm(request.POST or None)
  if form.is_valid():
    form.send_email(form.cleaned_data['name'])
    messages.success(request, 'Mensagem enviada com sucesso!')
  elif request.method == 'POST':
    messages.error(request, 'Formulário Inválido')
  context = {
    'form': form,
  }
  return render(request, template, context)
