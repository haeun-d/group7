from django.urls import path
from .views import *

app_name='consumption'

urlpatterns=[
    path('search/<str:nickname>/',main_consumption,name='consumption'),
    path('consumption-detail/<int:pk>/',consumption_detail.as_view(), name='consumption-detail'),
    path('calender/',calender, name="calender"),
    path('calender-update/<int:id>/', calender_update, name='calender-update'),
    path('record-delete/<int:id>/',delete, name="record-delete"),
    path('friend/',friend, name="friend"),
    path('search-friend/',search_friend, name="search-friend"),
    path('like/<int:id>/',like, name="like"),
    path('statistic/',statistic, name='statistic'),
    path('follow/<str:nickname>/', follow, name="follow"),
    path('unfollow/<str:nickname>/', unfollow, name="unfollow"),
    
]