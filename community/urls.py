from django.urls import path
from . import views
from .views import *

app_name = 'community'

urlpatterns = [
    path('',views.community_main, name="community-main"),
    path('food/',food,name='food'),
    path('delivery/', delivery, name='delivery'),
    path('create-post/',create_post,name='create-post'),
    path('delivery-post/',delivery_post, name='delivery-post'),
    path('food/<str:category>/',category_posts, name='category-posts'),
    path('delivery/<str:category_delivery>',category_delivery, name='category-delivery'),
    path('delete/<int:pk>/', delete_post, name='delete-post'),
    path('delete_delivery/<int:pk>/', delete_delivery, name='delete-delivery'),
    path('edit/<int:pk>/', views.edit_post, name='edit-post'),
    path('edit_delivery/<int:pk>', views.edit_delivery, name='edit-delivery'),
    path('search/',search,name='search'),
    path('search_delivery/',search_delivery,name='search-delivery'),
    #path('ott/',ott,name='ott'),
    path('food_detail/<int:pk>/', views.food_detail, name='food-detail'),
    path('delivery_detail/<int:pk>/', views.delivery_detail,name='delivery-detail'),
    path('comment/<int:pk>/', comment, name='comment'),
    path('comment_delivery<int:pk>/',comment_delivery,name='comment-delivery'),
    path('delete_comment/<int:pk>/',views.delete_comment,name='delete-comment'),
    path('delete_deliverycomment/<int:pk>/',views.delete_deliverycomment,name='delete-deliverycomment'),
]

