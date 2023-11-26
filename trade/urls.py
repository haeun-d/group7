from django.urls import path
from . import views

app_name='trade'

urlpatterns=[
    path('',views.trade_first,name='trade'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.trade_detail, name='trade_detail'),
    path('<int:pk>/edit/', views.edit_post, name='edit_post'),
    path('<int:pk>/delete/', views.delete_post, name='delete_post'),
    path('<int:pk>/chat/', views.chat, name='chat'),
]
