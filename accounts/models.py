from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
	ROLES = (
		('chef', 'CHEF'),
		('user', 'USER')
	)
	COUNTRIES = (
		('ng', 'NG'),
		('gh', 'GH'),
		('sa', 'SA')
	)
	role = models.CharField(max_length=5, choices=ROLES)
	country = models.CharField(max_length=5, choices=COUNTRIES)
