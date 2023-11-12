from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class CustomUserManager(BaseUserManager):
    def _create_user(self, username, email, password, **extra_fields):
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff',False)  #이메일 부분 제거 
        extra_fields.setdefault('is_superuser',False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff',True)  
        extra_fields.setdefault('is_superuser',True)
        return self._create_user(username, email, password, **extra_fields)


class User(AbstractUser):
    email = models.EmailField(max_length=30, unique=True, null=False, blank=False)
    nickname = models.CharField(max_length=20, default='덕우')

    objects = CustomUserManager()

    def __str__(self):
        return self.username