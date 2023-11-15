from django.db import models
from users.models import User
# Create your models here.
class Record(models.Model):
    CATEGORY=[
        ('음식','음식'),
        ('생필품','생필품'),
        ('여가','여가'),
        ('교통','교통'),
        ('학습','학습'),
        ('기타','기타'),
    ]
    year=models.IntegerField(verbose_name="년")
    month=models.IntegerField(verbose_name="월")
    date=models.IntegerField(verbose_name="일")
    price=models.IntegerField(verbose_name="소비금액")
    likes=models.IntegerField(default=0)
    name=models.CharField(verbose_name="구매물품",max_length=20)
    category=models.CharField(max_length=10, choices=CATEGORY)
    purpose=models.CharField(verbose_name="목적",max_length=20)
    share=models.BooleanField(verbose_name="공개여부", default=False)
    detail=models.TextField(verbose_name="상세정보")
    writer=models.ForeignKey(User, related_name="record_writer", on_delete=models.CASCADE)
    like_user=models.ManyToManyField(User, related_name="like_user")

    def __str__(self):
        return self.name

