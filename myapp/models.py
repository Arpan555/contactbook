from django.db import models

# Create your models here.
class ContactBook(models.Model):
	name=models.CharField(max_length=30)
	email=models.EmailField()
	number=models.CharField(max_length=15)
	address=models.CharField(max_length=100)

	def __str__(self):
		return self.name
	