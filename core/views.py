from django.shortcuts import render
from .forms import ContactForm


def home(request):
  template = 'core/home.html'
  form = ContactForm(request.POST or None)
  if form.is_valid():
    form.send_email(form.cleaned_data['name'])
  context = {
    'form': form,
  }
  return render(request, template, context)
