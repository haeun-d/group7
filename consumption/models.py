from django.db import models

# Create your models here.
class Record(models.Model):
    bank=models.CharField(max_length=30)
    
