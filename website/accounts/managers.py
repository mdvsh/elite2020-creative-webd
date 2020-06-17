# Import UserManager
from django.contrib.auth.models import BaseUserManager

# Class containing functions to create users
class UserManager(BaseUserManager):
    # https://docs.djangoproject.com/en/3.0/topics/migrations/#model-managers
    # force migration
    use_in_migration = True

    def _create_user(self, email, password, **extra_fields):
        if not email: raise ValueError('Email not provided.')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_staff', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        if extra_fields.get('is_superuser') is not True:
            raise ValueError()
        if extra_fields.get('is_staff') is not True:
            raise ValueError()
        return self._create_user(email, password, **extra_fields)