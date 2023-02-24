from django.db import models

# Create your models here.

dept=[('General Health','General Health'),('Cardiology','Cardiology'),('Dental','Dental')]
class Booking(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(null=True,blank=True)
    date=models.DateField(null=True,blank=True)
    department=models.CharField(max_length=100, choices=dept)
    message=models.TextField(max_length=100)


    def __str__(self):
        return self.name







