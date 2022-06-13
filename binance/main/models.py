from django.db import models
from django.utils import timezone
from django.urls import reverse 


class CoinName(models.Model):
	name = models.CharField(max_length=255)
	created = models.DateTimeField(default=timezone.now)

	class Meta:
		ordering = ('-created', )


class Coin(models.Model):
	name = models.CharField(max_length=255)
	slug = models.SlugField(max_length=255, unique=True)
	description = models.TextField()
	market_cap = models.BigIntegerField(default=0)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	created = models.DateTimeField(default=timezone.now)

	class Meta:
		ordering = ('-created', )


	def get_absolute_url(self):
		return reverse('detail', args=[self.slug])


class Comment(models.Model):
	coin = models.ForeignKey(Coin, on_delete=models.CASCADE, related_name='comments')
	name = models.CharField(max_length=255)
	body = models.TextField()
	created = models.DateTimeField(auto_now_add=True)
	active = models.BooleanField(default=True)