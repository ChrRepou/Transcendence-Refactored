#creating models that will then been created into tables

from django.db import models
from django.contrib.auth.models import AbstractUser, Group

class Player(AbstractUser):
	user_permissions = models.ManyToManyField(
		'auth.Permission',
		related_name='player_permissions',
		blank=True,
	)
	groups = models.ManyToManyField(
		Group,
		related_name='player_groups',
		blank=True,
	)

	# add additional fields in here
	wins = models.IntegerField(default=0)
	losses = models.IntegerField(default=0)

	def __str__(self):
		return self.username

