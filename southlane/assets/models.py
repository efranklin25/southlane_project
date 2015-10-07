from django.db import models
from treebeard.mp_tree import MP_Node

from users.models import User

## Models for the Asset Management Application -- These's models define the hierarchical datastructure for our dynamic asset managment system.  ##
## Categories must end in an (Object) type which then serves as the "template" for the subsequent Asset objects which are all unique ##

class Category(MP_Node):
	name = models.CharField(max_length=100)
	node_order_by = ['name']

	parent_category = models.ForeignKey(Category, blank=True) # If Category has no parent, it is a prime category
	TYPE_CHOICES = (
			('PRIME', 'Prime Category'),
			('SUB', 'Sub-Catagory'),
			('OBJ', 'Asset')
		)
	_type = models.CharField(max_length=15, choices=TYPE_CHOICES, default='OBJ')
	description = models.CharField(max_length=500)
	ISBN = models.CharField(max_length=13)
	model_number = models.CharField(max_length=100) 
	publish_date = models.DateFIeld()
	edition = models.CharField(max_length=50)
	author = models.CharField(max_length=300)
	publisher = models.CharField(max_length=300)
	vendor = models.CharField(max_length=300)
	value = models.DecimalField(max_digits=None, decimal_places=2)
	picture = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)	
	current = models.BooleanField() # Is this asset the most current, or is it out of date
	admin = models.ForiegnKey(User, blank=True) # If blank or null, then category must inhertit admin from parent category, prime category must have admin

class Asset(models.Model):
	active = models.BooleanField()
	asset_tag = models.CharField(db_index=True, max_length=10, primary_key=True)
	category = models.ForiegnKey(Category)
	feature = models.CharField(max_length=200)
	name = models.CharField(max_length=300)
	serial_number = models.CharField(max_length=100)
	CONDITION_CHOICES = (
			('10', 'New'),
			('8', 'Great'),
			('6', 'Good'),
			('4', 'Acceptable'),
			('2', 'Poor'),
			('0', 'Terrible')
		)
	condition = models.CharField(max_length=20, choices=CONDITION_CHOICES, default='10')
	possession = models.ForeignKey(User, blank=True) #Who has the asset right now
	consumables = models.ManyToManyField(Consumable)

	def __str__(self):
		return "%s %s" % (self.asset_tag, self.name)


class Consumable(models.Model):
	active = models.BooleanField()
	asset_tag = models.CharField(db_index=True, max_length=10, primary_key=True)
	inventory = models.IntegerField()
	name = models.CharField(max_length=300)
	description = models.TextField(max_length=500)
	picture = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)		
	author = models.CharField(max_length=300)
	publisher = models.CharField(max_length=300)
	model_number = models.CharField(max_length=100)
	value = models.DecimalField(max_digits=None, decimal_places=2)
	asset = models.ManyToManyField(Category)

	def __str__(self):
		return "%s %s" % (self.asset_tag, self.name)


