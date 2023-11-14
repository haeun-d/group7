from django.urls import path
from .views import *

app_name='consumption'

urlpatterns=[
    path('',main_consumption,name='main-consumption'),
]