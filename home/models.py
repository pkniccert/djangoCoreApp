from django.db import models

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
