from django.db import models

# Create your models here.

class Customer(models.Model):
    name= models.CharField(max_length=100, null=True, on_delete=models.CASCADE)
    contact = models.CharField(max_length=13, null=True)
    email = models.CharField(max_length=100, null= True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    address = models.CharField(max_length=200, null=True)
    