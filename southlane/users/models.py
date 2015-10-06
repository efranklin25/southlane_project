from django.db import models

class User(models.Model):
	active = models.BooleanField()
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	picture = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100, **options)
	role = **"Staff, Admin etc"**
	employeeID = models.CharField(max_length=50)
	userID = models.CharField(max_length=30)
	password = **PASSWORD**
	#Assets in posession =
	#Asset History = 
	#Consumables Taken = 
	#Session ID =
	#Session Expiration / management =