from django.db import models
from catalog.models import Product
from django.conf import settings


class CartItemManager(models.Manager):

  def add_item(self, cart_key, product):
    if self.filter(cart_key=cart_key, product=product).exists():
      created = False
      cart_item = self.get(cart_key=cart_key, product=product)
      cart_item.quantity += 1
      cart_item.save()
    else:
      created = True
      cart_item = CartItem.objects.create(cart_key=cart_key, product=product, price=product.price)
    return cart_item, created


class CartItem(models.Model):
  product = models.ForeignKey(Product, verbose_name='Produto')
  quantity = models.PositiveIntegerField('Quantidade', default=1)
  cart_key = models.CharField('Chave do carrinho', max_length=40, db_index=True)
  price = models.DecimalField('Preço', decimal_places=2, max_digits=8)

  objects = CartItemManager()

  def __str__(self):
    return '{} [{}]'.format(self.product, self.quantity)

  class Meta:
    verbose_name = 'Item do Carrinho'
    verbose_name_plural = 'Itens do Carrinho'
    # evita o mesmo produto com a mesma chave no banco de dados, ambos serão uma chave unica
    unique_together = (('cart_key', 'product'),)


class OrderManager(models.Manager):

  def create_order(self, user, cart_items):
    order = self.create(user=user)
    for item in cart_items:
      order_item = OrderItem.objects.create(
        order=order, quantity=item.quantity, product=item.product, price=item.price
      )
    return order


class Order(models.Model):
  STATUS_CHOICE = (
    (0, 'Aguardando pagamento'),
    (1, 'Concluído'),
    (2, 'Cancelado'),
  )
  PAYMENT_OPTION_CHOICES = (
    ('deposit', 'Depósito'),
    ('pagseguro', 'PagSeguro'),
    ('paypal', 'Paypal'),
  )
  user = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Usuário")
  status = models.IntegerField('Situação', choices=STATUS_CHOICE, default=0, blank=True)
  payment_option = models.CharField('Opção de pagamento', choices=PAYMENT_OPTION_CHOICES, default='deposit', max_length=20)
  created_at = models.DateTimeField('Criado em', auto_now_add=True)
  updated_at = models.DateTimeField('Atualizado em', auto_now=True)

  objects = OrderManager()

  def __str__(self):
    return 'Pedido #{}'.format(self.pk)

  class Meta:
    verbose_name = 'Pedido'
    verbose_name_plural = 'Pedidos'


class OrderItem(models.Model):
  order = models.ForeignKey(Order, verbose_name="Pedido", related_name='items')
  product = models.ForeignKey(Product, verbose_name='Produto')
  quantity = models.PositiveIntegerField('Quantidade', default=1)
  price = models.DecimalField('Preço', decimal_places=2, max_digits=8)

  def __str__(self):
    return '[{}] - {}'.format(self.order, self.product)

  class Meta:
    verbose_name = 'Item do pedido'
    verbose_name_plural = 'Itens do pedido'


def post_save_cart_item(instance, **kwargs):
  if instance.quantity < 1:
    instance.delete()


models.signals.post_save.connect(post_save_cart_item, sender=CartItem, dispatch_uid='post_save_cart_item')

