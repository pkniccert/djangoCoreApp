from django.db import models

# Create your models here.

class Recipe(models.Model):
    recipe_name = models.CharField(max_length=100)
    recipe_descrition = models.TextField()
    recipe_image = models.ImageField(upload_to="uploads/recipes/")
