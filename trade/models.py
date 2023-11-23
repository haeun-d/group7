from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    price = models.CharField(max_length=50)
    head_image = models.ImageField(upload_to='trade/images/%Y/%m/%d/', blank=True)
    place = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'[{self.pk}]{self.title}'
    def get_absolute_url(self):
        return f'/trade/{self.pk}/'
