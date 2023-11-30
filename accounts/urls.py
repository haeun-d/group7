from django.urls import path
from .views import *

app_name = 'accounts'

urlpatterns=[
    path('signup/',signup_view, name='signup'),
    path('login/',login_view,name='login' ),
    path('logout/',logout_view, name='logout'),
    path('mypage/',mypage,name="mypage"),
    path('update-user-info/',update_userinfo, name='update-user-info'),
    path('my-benefit-scrap',benefit_scrap, name='benefit-scrap'),
    path('my-map-scrap',map_scrap, name='map-scrap'),
    path('my-trade',my_trade, name='my-trade'),
    path('my-trade-detail/<int:post_id>/',my_trade_detail, name='my-trade-detail'),
    path('chatroom/<int:post_id>/',seller_chat, name='seller-chat'),
    path('proceeding-chat',proceeding_chat, name='proceeding-chat'),
    path('leave-chat-room/<int:room_id>/',leave_chat_room, name='leave-chat-room'),
    path('review-list/',review_make, name='review-list'),
    path('my-post-food/',my_post_food, name='my-post-food'),
    path('my-post-ott/',my_post_ott, name='my-post-ott'),
]