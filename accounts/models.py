from django.db import models
from django.contrib.auth.models import AbstractUser
from .utils import generate_default_username
from .manager import UserManager
# Create your models here.

class CustomUser(AbstractUser):
    username = models.CharField(max_length=150, unique=True, default=generate_default_username())
    phone_number = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    user_bio = models.CharField(max_length=50, blank=True)
    user_profile_image = models.ImageField(upload_to="uploads/profile", blank=True, null=True)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'