from django.urls import path
from .views import *

app_name='map'

urlpatterns=[
    path('',map_benefit_list, name='map-benefit'),
    path('map-detail/<int:pk>/',map_detail.as_view(), name='map-detail'),
    path('benefit-detail/<int:pk>/', benefit_detail.as_view(), name='benefit-detail'),

]