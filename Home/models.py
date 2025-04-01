from django.db import models
from django.contrib.auth.models import User 
import datetime


class Package(models.Model):  
    pName = models.CharField(max_length=100, primary_key=True, verbose_name="Package Name")  
    destination = models.CharField(max_length=100, verbose_name="Destination")
    hotel = models.CharField(max_length=100, verbose_name="Hotel Name")
    days = models.IntegerField(verbose_name="Number of Days")
    nights = models.IntegerField(verbose_name="Number of Nights")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Package Price")  
    description = models.TextField(verbose_name="Package Description")  
    imgname = models.CharField(max_length=100, verbose_name="Image Name")

    def __str__(self):
        return f"{self.pName} - {self.destination}"


 

class Booking(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    numberofpeople = models.IntegerField(default=1)  
    date = models.DateField(default=datetime.date.today)  
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  
    status = models.CharField(max_length=20)

    def save(self, *args, **kwargs):
        
        if self.package and self.numberofpeople is not None:
            self.total_price = self.package.price * self.numberofpeople
        else:
            self.total_price = 0  
        
        super().save(*args, **kwargs)  


