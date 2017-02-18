from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, TemplateView, UpdateView, FormView
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm, SetPasswordForm
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .forms import PasswordResetForm, UserAdminCreationForm
from .models import PasswordReset, User
from .serializers import UserSerializer


class RegisterView(CreateView):
  model = User
  template_name = 'accounts/register.html'
  form_class = UserAdminCreationForm
  success_url = reverse_lazy('accounts:profile')


class ProfileView(LoginRequiredMixin, TemplateView):
  template_name = 'accounts/profile.html'


class UpdateUserView(LoginRequiredMixin, UpdateView):
  model = User
  template_name = 'accounts/edit.html'
  fields = ['username', 'name', 'email', 'country', 'city', 'state', 'complement', 'DDD', 'number']
  success_url = reverse_lazy('accounts:profile')

  def get_object(self):
    return self.request.user

  def form_valid(self, form):
    messages.success(self.request, "Seus dados foram atualizados com sucesso")
    return super(UpdateUserView, self).form_valid(form)


class UpdatePasswordView(LoginRequiredMixin, FormView):
  template_name = 'accounts/edit_password.html'
  success_url = reverse_lazy('accounts:profile')
  form_class = PasswordChangeForm

  def get_form_kwargs(self):
    kwargs = super(UpdatePasswordView, self).get_form_kwargs()
    kwargs['user'] = self.request.user
    return kwargs

  def form_valid(self, form):
    form.save()
    messages.success(self.request, "Sua senha foi atualizada com sucesso")
    return super(UpdatePasswordView, self).form_valid(form)


def reset_password(request):
  template = 'accounts/reset_password.html'
  form = PasswordResetForm(request.POST or None)
  context = {}
  if form.is_valid():
    form.save()
    context['success'] = True
  context['form'] = form
  return render(request, template, context)


def reset_password_confirm(request, key):
  template = 'accounts/reset_password_confirm.html'
  context = {}
  reset = get_object_or_404(PasswordReset, key=key)
  form = SetPasswordForm(user=reset.user, data=request.POST or None)
  if form.is_valid():
    form.save()
    context['success'] = True
  context['form'] = form
  return render(request, template, context)



class UserList(APIView):

  def get(self, request, *args, **kwargs):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)
