from django.conf.urls import url
from . import views

app_name='catalog'
urlpatterns = [
  url(r'^$', views.product_list, name='product_list'),
  url(r'^(?P<category_slug>[\w_-]+)/$', views.category, name='category'),
  url(r'^produto/(?P<product_slug>[\w_-]+)/$', views.product, name='product'),
]
