from django.shortcuts import render, redirect
from .forms import  SignUpForm
# Create your views here.

def signup_view(request):
    if request.method == "GET":
        form = SignUpForm()
        context = {'form': form}
        return render(request, 'accounts/signup.html', context)

    form = SignUpForm(request.POST)
    if form.is_valid():
        print(f"Redirecting to: {redirect('index').url}")  # 추가된 부분
        instance = form.save()
        return redirect('index')
    else:
        print(form.errors)
        return render(request, 'accounts/signup.html', {'form': form})


