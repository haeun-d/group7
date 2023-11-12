from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *
from datetime import date

def map_benefit_list(request):
    today = date.today()
    benefits = Benefit.objects.filter(deadline__gte=today).order_by('deadline') # 날짜가 지난 데이터들은 불러오지 않음 deadline>today
    maps=Map.objects.all()
    context={'benefits':benefits, 'maps':maps}
    return render(request, 'map/map_benefit.html',context)

class map_detail(DetailView):
    model=Map


class benefit_detail(DetailView):
    model=Benefit