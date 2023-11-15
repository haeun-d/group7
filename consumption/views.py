from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime
from .models import Record
from users.models import *
from django.http import Http404
from django.views.generic import  DetailView
# Create your views here.
y = [n for n in range(2023, 1999, -1)]
m=[n for n in range(1,13)]
d=[n for n in range(1,32)]

def parseTime(date):
    m=date[0:2]
    d=date[3:5]
    y=date[6:10]
    return y,m,d

def common_category(a,b,c,d,e,f):
    max_count=max(a, b, c, d, e)
    common_category_list=[]
    if max_count == a:
        common_category_list.append("음식")
    elif max_count == b:
        common_category_list.append("생필품")
    elif max_count == c:
        common_category_list.append("여가")
    elif max_count == d:
        common_category_list.append("교통")
    elif max_count == e:
        common_category_list.append("학습")
    elif max_count == e:
        common_category_list.append("기타")

    return common_category_list

def main_consumption(request, username):
    request.session['username'] = username
    user = User.objects.get(username=username)
    print(user.like_user.all())
    

    if(request.user==user):
        me=True
    else:
        me=False

    if request.method=="GET":
        today=datetime.today().strftime("%m/%d/%Y")
        year, month, date=parseTime(today)
    else:
        year=request.POST.get('year')
        month=request.POST.get('month')
        date=request.POST.get('date')

    print(username)
    print(request.user.username)

    records=Record.objects.filter(writer=user, year=year, month=month, date=date).order_by('category')
    category=["음식","생필품","여가","교통","학습","기타"]
    context={
        "find_y":year,
        "find_m":month,
        "find_d":date,
        "year":y,
        "month":m,
        "date":d,
        "records":records,
        "category":category,
        "username":username
    }
    return render(request, 'consumption/my_consumption.html', context)
        
class consumption_detail(DetailView):
    model=Record

def calender_update(request, id):
    record=get_object_or_404(Record, id=id)
    if request.method=="POST":
        full_date=request.POST.get('full_date')
        price=request.POST.get('price')
        name=request.POST.get('name')
        category=request.POST.get('category')
        purpose=request.POST.get('purpose')
        share=request.POST.get('share')
        detail=request.POST.get('detail')
        share = request.POST.get('share') == "True"
        year, month, date=parseTime(full_date)
        record.year=year
        record.month=month
        record.date=date
        record.price=price
        record.name=name
        record.category=category
        record.purpose=purpose
        record.share=share
        record.detail=detail
        record.writer=request.user
        record.save()
        return redirect('consumption:my-consumption', request.user.username)
    else:
        return render(request, 'consumption/calener_update.html',{"record":record})

def calender(request):
    if request.method=="GET":
        return render(request, 'consumption/calender.html')
    else:
        full_date=request.POST.get('full_date')
        price=request.POST.get('price')
        name=request.POST.get('name')
        category=request.POST.get('category')
        purpose=request.POST.get('purpose')
        share=request.POST.get('share')
        detail=request.POST.get('detail')
        share = request.POST.get('share') == "True"
        year, month, date=parseTime(full_date)
        Record.objects.create(
            year=year,
            month=month,
            date=date,
            price=price,
            name=name,
            category=category,
            purpose=purpose,
            share=share,
            detail=detail,
            writer=request.user
        )
        return redirect('consumption:my-consumption', request.user.username)


def delete(request, id):
    record=get_object_or_404(Record, id=id)
    record.delete()
    return redirect('consumption:my-consumption', request.user.username)


def friend(request):
    following=request.user.following.all()
    following_array=[n.following for n in following]

    context={
        "following":following_array,
    }
    return render(request, 'consumption/friend.html', context)

def search_friend(request):
    if request.method=="POST":
        search=request.POST.get("search")
        request.session['search'] = search
        users=User.objects.filter(username__contains=search)
    else:
        try:
            users=User.objects.filter(username__contains=request.session['search'])
        except:
            users=None
    following=request.user.following.all() 
    following_username_array=[n.following.username for n in following]
    context={
        "following":following_username_array,
        "users":users
    }
    return render(request, 'consumption/search_friend.html', context)

def follow(request, username):
    following=User.objects.get(username=username)
    Follow.objects.create(follower=request.user, following=following)
    return redirect("consumption:search-friend")

def unfollow(request,username):
    unfollowing=User.objects.get(username=username)
    relation=Follow.objects.filter(follower=request.user, following=unfollowing)
    relation.delete()
    return redirect("consumption:search-friend")

def like(request, id):
    print("in")
    record=get_object_or_404(Record, id=id)
    if request.user not in record.like_user.all():
        record.like_user.add(request.user)
        record.likes+=1
    else:
        record.like_user.remove(request.user)
        record.likes-=1
    record.save()
    print(record.like_user.all())
    print("in")
    return redirect('consumption:my-consumption', request.session['username'])

def statistic(request):
    if request.method=="POST":
        year=request.POST.get("year")
        month=request.POST.get("month")
    else:
        today=datetime.today().strftime("%m/%d/%Y")
        year, month, date=parseTime(today)
    total=Record.objects.filter(writer=request.user, year=year, month=month).count()
    food=Record.objects.filter(writer=request.user, category="음식", year=year, month=month)
    life=Record.objects.filter(writer=request.user, category="생필품", year=year, month=month)
    leisure=Record.objects.filter(writer=request.user, category="여가", year=year, month=month)
    transportation=Record.objects.filter(writer=request.user, category="교통", year=year, month=month)
    study=Record.objects.filter(writer=request.user, category="학습", year=year, month=month)
    etc=Record.objects.filter(writer=request.user, category="기타", year=year, month=month)
    
    total_records= Record.objects.filter(writer=request.user, year=year, month=month)
    common_category_array=common_category(food.count(),life.count(),leisure.count(),transportation.count(),study.count(),etc.count())
    
    # 통계
    try:
        food_p = (food.count() / total) * 100
        life_p = (life.count() / total) * 100
        leisure_p = (leisure.count() / total) * 100
        transportation_p = (transportation.count() / total) * 100
        study_p = (study.count() / total) * 100
        etc_p = (etc.count() / total) * 100
        
    except:
        food_p=life_p=leisure_p=transportation_p=study_p=etc_p=0
        common_category_array=[]

    value=[food_p, life_p, leisure_p, transportation_p, study_p, etc_p]
    value=','.join(map(str,value))
    context={
        "common_category":common_category_array,
        "value":value,
        "year":y,
        "month":m,
        "find_y":year,
        "find_m":month,
        "total_consumed":sum(record.price for record in total_records),
        "food_c":sum(record.price for record in food),
        "life_c":sum(record.price for record in life),
        "leisure_c":sum(record.price for record in leisure),
        "transportation_c":sum(record.price for record in transportation),
        "study_c":sum(record.price for record in study),
        "etc_c":sum(record.price for record in etc),
        
    }
    return render(request, 'consumption/statistics.html', context)
