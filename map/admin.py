from django.contrib import admin
from .models import *
# Register your models here.
class BenefitPhotoInline(admin.TabularInline):
    model=BenefitPhoto


class MapPhotoInline(admin.TabularInline):
    model = MapPhoto


@admin.register(Benefit)
class BenefitAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines=[BenefitPhotoInline]


@admin.register(Map)
class MapAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines=[MapPhotoInline]