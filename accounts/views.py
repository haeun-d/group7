from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from .forms import  SignUpForm

# 회원가입
def signup_view(request):
    if request.method == "GET":
        form = SignUpForm()
        context = {'form': form}
        return render(request, 'accounts/signup.html', context)
    form = SignUpForm(request.POST, request.FILES)
    # 유효한 내용인지 확인
    if form.is_valid():
        user = form.save()
        return redirect('main')
    else:
        return render(request, 'accounts/signup.html', {'form': form})


def login_view(request):
    if request.method=="GET":
        return render(request, 'accounts/login.html', {'form':AuthenticationForm})

    form=AuthenticationForm(request, data=request.POST)
    if form.is_valid():
        login(request, form.user_cache)
        return redirect('main')
    return render(request, 'accounts/login.html',{'form':form})

def logout_view(request):
    if request.user.is_authenticated:
        logout(request)

    return redirect('main')

def mypage(request):
    return render(request, 'accounts/mypage.html')

def update_userinfo(request):
    if request.method=="POST":
        nickname=request.POST.get('nickname')
        email=request.POST.get('email')
        new_profile=request.FILES.get('profile')
        if new_profile:
            request.user.profile.delete()
            request.user.profile=new_profile
        request.user.nickname=nickname
        request.user.email=email
        request.user.save()
        return redirect('accounts:mypage')
    return render(request, 'accounts/update_userinfo.html')

def benefit_scrap(request):
    benefits=request.user.scrap_benefits.all()
    context = {
        'benefits': benefits
    }
    return render(request, 'accounts/benefit_scrap.html', context)

def map_scrap(request):
    maps=request.user.map_benefits.all()
    context={
        'maps':maps
    }
    return render(request, 'accounts/map_scrap.html', context)
