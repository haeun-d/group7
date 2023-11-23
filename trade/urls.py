from django.urls import path
from . import views

app_name='trade'

urlpatterns=[
    path('',views.trade_first,name='trade'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.trade_detail, name='trade_detail'),
]
