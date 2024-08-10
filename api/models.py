from django.db import models
from django.contrib.auth import get_user_model
from .validators import chef_role_only, user_role_only

User = get_user_model()

# Create your models here.


class Menu(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, validators=[chef_role_only])
	name = models.CharField(max_length=255)
	description = models.TextField()
	price = models.DecimalField(max_digits=6, decimal_places=2)

	def __str__(self):
		return self.name

class Booking(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, validators=[user_role_only])
	menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now_add=True)
	venue = models.TextField()
	amount_of_guests = models.IntegerField()

	def __str__(self):
		return f'Booking {self.pk}'
