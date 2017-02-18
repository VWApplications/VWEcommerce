from django.conf.urls import url
from django.contrib.auth.views import login, logout
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = 'accounts'
urlpatterns = [
  url(r'^$', views.ProfileView.as_view(), name="profile"),
  url(r'^entrar/$', login, {'template_name': 'accounts/login.html'}, name="login"),
  url(r'^sair/$', logout, {'next_page': 'core:home'}, name="logout"),
  url(r'^cadastrar/$', views.RegisterView.as_view(), name="register"),
  url(r'^editar/$', views.UpdateUserView.as_view(), name="edit"),
  url(r'^editar-senha/$', views.UpdatePasswordView.as_view(), name="edit_password"),
  url(r'^resetar-senha/$', views.reset_password, name="reset_password"),
  url(r'^confirmar-nova-senha/(?P<key>\w+)/$', views.reset_password_confirm, name="reset_password_confirm"),
  url(r'^users.json', views.UserList.as_view(), name="user_json")
]

urlpatterns = format_suffix_patterns(urlpatterns)
