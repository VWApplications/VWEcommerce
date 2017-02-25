from django.conf.urls import url
from . import views

app_name='checkout'
urlpatterns = [
  url(r'^$', views.CartItemView.as_view(), name='cart'),
  url(r'^adicionar/(?P<product_slug>[\w_-]+)$', views.CreateCartItemView.as_view(), name='create-cartitem'),
  url(r'^checkout/$', views.CheckoutView.as_view(), name='checkout')
]
