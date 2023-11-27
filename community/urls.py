from django.urls import path
from . import views
from .views import *

app_name = 'community'

urlpatterns = [
    #path('', views.PostList.as_view()),
    #path('<int:pk>/', views.PostDetail.as_view()),
    path('community/',views.community_main, name="community-main"),
    path('food/',food,name='food'),
    #path('food/',FoodListView.as_view(), name='food'),
    path('delivery/', delivery, name='delivery'),
    #path('food-post/',food_post,name='food-post'),
    #path('delivery-post/',delivery_post,name='delivery-post'),
    path('create-post/',create_post,name='create-post'),
    path('delivery-post/',delivery_post, name='delivery-post'),
    path('food/<str:category>/',category_posts, name='category-posts'),
    path('delivery/<str:category_delivery>',category_delivery, name='category-delivery'),
    path('delete/<int:pk>/', delete_post, name='delete-post'),
    #path('edit/<int:pk>/', edit_post, name='edit-post'),
    path('edit/<int:pk>/', views.edit_post, name='edit-post'),
    path('edit_delivery/<int:pk>', views.edit_delivery, name='edit-delivery'),
    path('search/',search,name='search'),
    path('search_delivery/',search_delivery,name='search-delivery'),
    path('ott/',ott,name='ott'),
    path('detail/<int:pk>/', views.food_detail, name='food-detail'),
    path('detail/<int:pk>/', views.delivery_detail,name='delivery-detail'),
    path('comment/<int:pk>/', comment, name='comment'),
]

