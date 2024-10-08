from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()


class RecipesManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted = False)


class StudentsManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted = False)

# Create your models here.

class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    recipe_name = models.CharField(max_length=100)
    recipe_descrition = models.TextField()
    recipe_image = models.ImageField(upload_to="uploads/recipes/")
    recipe_view_count = models.IntegerField(default=1)
    is_deleted = models.BooleanField(default=False)

    objects = RecipesManager()
    admin_objects = models.Manager()

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
class Subject(models.Model):
    subject_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.subject_name

class Student(models.Model):
    department = models.ForeignKey(Department, related_name="depart", on_delete=models.CASCADE)
    student_id = models.OneToOneField(StudentID, related_name="studentid", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.TextField(null=True, blank=True)
    is_deleted = models.BooleanField(default=False)

    objects = StudentsManager()
    admin_objects = models.Manager()

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        ordering = ['name']
        verbose_name = "student"


class SubjectMarks(models.Model):
    student = models.ForeignKey(Student, related_name="studentmarks", on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks = models.IntegerField()

    def __str__(self) -> str:
        return f'{self.student.name} {self.subject.subject_name}'
    
    class Meta:
        unique_together = ['student', 'subject']

class ReportCard(models.Model):
    student = models.ForeignKey(Student, related_name="studentreportcard", on_delete=models.CASCADE) 
    student_rank = models.IntegerField()
    date_of_report_card_generation = models.DateField(auto_now_add=True)

    class Meta:
        unique_together = ['student_rank', 'date_of_report_card_generation']