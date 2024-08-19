from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    age = models.IntegerField()
    address = models.TextField(null=True, blank=True)
    file = models.FileField()

class Product(models.Model):
    title = models.TextField()
    description = models.TextField()

    def __str__(self) -> str:
        return self.title + " " + self.description
    

class Car(models.Model):
    car_name = models.CharField(max_length=500)
    speed = models.IntegerField(default=50)

    def __str__(self) -> str:
        return self.car_name

@receiver(pre_save, sender = Car)
def call_car_api(sender, instance, **kwargs):
    print("Car Object|Created")
    print(sender, instance, kwargs)