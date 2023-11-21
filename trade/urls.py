from django.urls import path
from . import views
import trade.views

app_name='trade'

urlpatterns=[
    path('',views.trade_first,name='trade')
]
