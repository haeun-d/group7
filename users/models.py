from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.validators import MinValueValidator, MaxValueValidator


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
    nickname = models.CharField(max_length=20,unique=True)
    profile=models.ImageField(upload_to="profile/", null=True)
    grade=models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(5)], default=5 )
    review_count=models.IntegerField(default=1)
    objects = CustomUserManager()
    def __str__(self):
        return self.username
    
    
class Follow(models.Model):
    follower = models.ForeignKey(User, related_name='following', on_delete=models.CASCADE)
    following = models.ForeignKey(User, related_name='followers', on_delete=models.CASCADE)
