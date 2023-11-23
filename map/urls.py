from django.urls import path
from .views import *

app_name='map'

urlpatterns=[
    path('',map_benefit_list, name='map-benefit'),
    path('map-detail/<int:pk>/',map_detail.as_view(), name='map-detail'),
    path('benefit-detail/<int:pk>/', benefit_detail.as_view(), name='benefit-detail'),
    path('scrap-benefit/<int:id>/',benefit_scrap, name='benefit-scrap'),
    path('scrap-map/<int:id>/',map_scrap, name='map-scrap'),
    path('mypage/benefit-detail/<int:id>/',benefit_scrap_detail, name='benefit-scrap-detail'),
    path('mypage/map-detail/<int:id>/',map_scrap_detail, name='map-scrap-detail'),
    
]