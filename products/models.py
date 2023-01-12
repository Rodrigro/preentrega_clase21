from django.db import models

# Create your models here.



class Camisetas(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    stock = models.BooleanField(default=True)
    
    
class Acesories(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    stock = models.BooleanField(default=True)    
    
    
class Calzados(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    stock = models.BooleanField(default=True)   
    size = models.FloatField() 