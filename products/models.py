from django.db import models


# Create your models here.

		


class PlateManager(models.Manager):

	def get_actives_plates(self):
		return self.filter(is_active=True)

	

class Plate(models.Model):
	name=models.CharField(max_length=50)
	description=models.TextField()
	is_active=models.BooleanField(default=True)
	price = models.DecimalField(max_digits=9,decimal_places=2)
	image=models.ImageField(upload_to='static/dynamic/products')

	@models.permalink
	def get_absolute_url(self):
		pass

	def __unicode__(self):
		return self.name

	objects=PlateManager()



