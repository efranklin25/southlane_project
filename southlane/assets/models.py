from django.db import models

from users.models import User

class AssetType(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=300)
	picture = 
	rules =
	admin = models.ForiegnKey(User)

class Asset(models.Model):
	active = models.BooleanField()
	asset_tag = models.CharField(max_length=10)
	name = models.CharField(max_length=300)
	description = models.TextField(max_length=500)
	picture = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, **options)
	ISBN =
	author =
	publisher =
	value = # Original Cost $$.$$
	#source = models.ForeignKey(Vendor) 
	model_number = 
	serial_number =
	condition = 
	publish_date =
	revision_date =
	current = 
	possession = models.OneToOneField(User, primary_key=True) #Who has the asset right now
	history =
	consumables = models.ManyToManyField(Consumable)


class Consumable(models.Model):
	active = models.BooleanField()
	asset_tag = models.CharField(max_length=10)
	inventory = #how many do we have
	name = models.CharField(max_length=300)
	description = models.TextField(max_length=500)
	picture = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, **options)		
	author =
	publisher =
	model_number =
	history = #Who has taken them, when and how many
	value = #cost per consumable
	asset = models.ManyToManyField(Asset)

class AssetHistory(models.Model):
	asset = models.OneToOneField(Asset)
	user =
	date_in =
	date_out =
	time_out =
	time_in =

class ConsumableHistory(models.Model):
	consumable = models.OneToOneField(Consumable)
	user =
	date_taken =
	time_taken =
	quantity_taken =

