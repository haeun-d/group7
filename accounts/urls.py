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
]