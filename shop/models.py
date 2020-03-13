from django.db import models

class Product(models.Model):
	product_id=models.AutoField
	# as we didn't assigned any primary key so it will take id as a primary key
	product_name=models.CharField(max_length=50)
	category=models.CharField(max_length=50,default="")
	subcategory=models.CharField(max_length=50,default="")
	price=models.IntegerField(default=0)
	product_time=models.DateField()
	dsec=models.CharField(max_length=200)
	image=models.ImageField(upload_to="shop/images",default="")

	def __str__(self):
 		return self.product_name
 

class Contact(models.Model):
	msg_id=models.AutoField(primary_key=True)
	# as we didn't assigned any primary key so it will take id as a primary key
	name=models.CharField(max_length=50,default="")
	email=models.CharField(max_length=50,default="")
	desc=models.CharField(max_length=50,default="")
	

	def __str__(self):
 		return self.name
 

class Orders(models.Model):
	order_id=models.AutoField(primary_key=True)
	# as we didn't assigned any primary key so it will take id as a primary key
	item_json=models.CharField(max_length=500)
	name=models.CharField(max_length=100)
	email=models.CharField(max_length=100)
	address=models.CharField(max_length=400)
	city=models.CharField(max_length=20)
	state=models.CharField(max_length=29)
	zip_code=models.CharField(max_length=6)
	def __str__(self):
 		return self.name
 
 	
# Create your models here.
