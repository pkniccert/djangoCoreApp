from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):

    def create_user(self, phone_number, password=None, **extra_fields):
        """
        Create and return a regular user with an email and password.
        """
        if not phone_number:
            raise ValueError("The Phone number field must be set")
        
        # Handle additional fields, normalize email if present
        extra_fields.setdefault('is_active', True)

        # Create user instance
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        """
        Create and return a superuser with an email and password.
        """
        # Set default values for superuser attributes
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(phone_number, password, **extra_fields)
