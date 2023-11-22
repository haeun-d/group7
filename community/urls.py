from django.urls import path
from . import views
from .views import *

app_name = 'community'

urlpatterns = [
    #path('', views.PostList.as_view()),
    #path('<int:pk>/', views.PostDetail.as_view()),
    path('community-main/',community_main, name="community-main"),
    path('food/',food,name='food'),
    path('delivery/', delivery, name='delivery'),
    path('food-post/',food_post,name='food-post'),
    path('delivery-post/',delivery_post,name='delivery-post'),
    path('create-post/',create_post,name='create-post'),
    path('search/',search,name='search'),

]

