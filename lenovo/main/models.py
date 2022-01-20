from django.db import models

# Create your models here.
class Buyer(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    address= models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Machine(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Sale(models.Model):
    c_id = models.ForeignKey(Buyer, on_delete=models.CASCADE) 
    p_id = models.ForeignKey(Machine, on_delete=models.CASCADE)
    price = models.IntegerField()

    def __int__(self):
        return self.price           
            
