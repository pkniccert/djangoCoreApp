from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    recipe_name = models.CharField(max_length=100)
    recipe_descrition = models.TextField()
    recipe_image = models.ImageField(upload_to="uploads/recipes/")
    recipe_view_count = models.IntegerField(default=1)

class Department(models.Model):
    department = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.department
    
    class Meta:
        ordering = ['department']

class StudentID(models.Model):
    student_id = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.student_id
    
class Student(models.Model):
    department = models.ForeignKey(Department, related_name="depart", on_delete=models.CASCADE)
    student_id = models.OneToOneField(StudentID, related_name="studentid", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ['name']
        verbose_name = "student"


