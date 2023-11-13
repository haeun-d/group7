from django.db import models

# Create your models here.
class Map(models.Model):
    latitude = models.FloatField(verbose_name="위도", default=0.0)  # 지도에 표시하기 위함
    longtitude = models.FloatField(verbose_name="경도", default=0.0)
    title=models.CharField(verbose_name="제목", max_length=100)
    place=models.CharField(verbose_name="위치", max_length=100)
    introduction = models.CharField(verbose_name="간단한 소개", max_length=100)
    deadline=models.DateField(verbose_name="마감일")
    detail=models.TextField(verbose_name="상세 설명")
    inquiry=models.TextField(verbose_name="문의")

class Benefit(models.Model):
    title = models.CharField(verbose_name="제목", max_length=100)
    introduction = models.CharField(verbose_name="간단한 소개", max_length=100)
    deadline = models.DateField(verbose_name="마감일")
    detail = models.TextField(verbose_name="상세 설명")
    inquiry = models.TextField(verbose_name="문의")

# 이미지 여러개 등록
class BenefitPhoto(models.Model):
    benefit = models.ForeignKey(Benefit, related_name='benefit_image', on_delete=models.CASCADE, null=True)
    image = models.ImageField('IMAGE', upload_to="benefit_image")

class MapPhoto(models.Model):
    benefit = models.ForeignKey(Map, related_name='map_image', on_delete=models.CASCADE, null=True)
    image = models.ImageField('IMAGE', upload_to="map_image")
