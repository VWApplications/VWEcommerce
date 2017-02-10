from django.shortcuts import render


def home(request):
  template = 'core/home.html'
  return render(request, template)
