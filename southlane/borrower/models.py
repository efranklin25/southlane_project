from django.db import models

from users.models import User
from assets.models import Asset, Consumable, Category

## Models for the borrower application -- Models responsible for storing the dates/times of checkouts and checkins, along with consumption of consumables by the users
## Also much manage the waiting list


class AssetEvent(models.Model):
	asset = models.ForeignKey(Asset)
	user = models.ForeignKey(User)
	check_out = models.DateTimeField(auto_now=False, auto_now_add=True)
	check_in = models.DateTimeField(auto_now=False, auto_now_add=False)

class ConsumableEvent(models.Model):
	consumable = models.ForeignKey(Consumable)
	user = models.ForeignKey(User)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	quantity_taken = models.IntegerField()

class WaitingList(models.Model):
	category = models.ForeignKey(Category)
	user = models.ForeignKey(User)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	time_needed = models.DateTimeField(auto_now=False, auto_now_add=False)

class Transfers(models.Model):
	asset = models.ForeignKey(Asset)
	sender = models.ForeignKey(User)
	reciever = models.ForeignKey(User)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	accepted = models.BooleanField()

	