from django.db import models
from catalog.models import Product


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


def post_save_cart_item(instance, **kwargs):
  if instance.quantity < 1:
    instance.delete()


models.signals.post_save.connect(post_save_cart_item, sender=CartItem, dispatch_uid='post_save_cart_item')

