from django.db import models

# Create your models here.


class Contact(models.Model):
	Name =models.CharField(max_length=25,blank=False)
	Email =models.EmailField(max_length=25)
	Phone =models.IntegerField()
	Message =models.TextField()
	def __str__(self):
		return self.Name


