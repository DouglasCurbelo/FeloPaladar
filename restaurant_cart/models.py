from django.db import models
from products.models import Plate 

# Create your models here.
class CartItem(models.Model):
	cart_id=models.CharField(max_length=50)
	quantiy=models.IntegerField(default=1)
	product=models.ForeignKey('products.Plate', unique=False)

	def total(self):
		return self.quantity * self.product.price

	def name(self):
		return self.product.name

	def price(self):
		return self.product.price

	def augment_quantity(self, quantity):
		self.quantity = self.quantity + int(quantity)
		self.save()

